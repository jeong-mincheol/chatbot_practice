<template>
  <div>
    <h2>KBO 선수 목록</h2>
    <table border="1">
      <thead>
        <tr>
          <th>KBO ID</th>
          <th>이름</th>
          <th>팀</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="player in paginatedPlayers" :key="player.kbo_id">
          <td>{{ player.kbo_id }}</td>
          <td>{{ player.name }}</td>
          <td>{{ player.team }}</td>
        </tr>
      </tbody>
    </table>

    <!-- 페이징 버튼 -->
    <div style="margin-top: 10px;">
      <button @click="goToPrev" :disabled="currentPage === 1">이전</button>
      ({{ currentPage }} / {{ totalPages }})
      <button @click="goToNext" :disabled="currentPage === totalPages">다음</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const players = ref([])
const currentPage = ref(1)
const pageSize = 10

// 페이징된 데이터 계산
const paginatedPlayers = computed(() => {
  const start = (currentPage.value - 1) * pageSize
  return players.value.slice(start, start + pageSize)
})

// 총 페이지 수
const totalPages = computed(() =>
  Math.ceil(players.value.length / pageSize)
)


const fetchPlayers = async () => {
  const res = await fetch('http://localhost:8000/items')
  const data = await res.json()
  players.value = data
}

const goToPrev = () => {
  if (currentPage.value > 1) currentPage.value--
}

const goToNext = () => {
  if (currentPage.value < totalPages.value) currentPage.value++
}

onMounted(fetchPlayers)
</script>

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border: 1px solid #aaa;
  padding: 8px;
  text-align: center;
}

thead {
  background-color: #f2f2f2;
}
</style>
