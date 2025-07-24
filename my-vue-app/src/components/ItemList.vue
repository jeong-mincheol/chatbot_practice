<template>
  <div>
    <h2>Item List</h2>
    <ul>
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ItemList",
  data() {
    return {
      items: []
    };
  },
  async mounted() { // 컴포넌트가 브라우저에 표시될 때 실행
    console.log('실행확인');
    try {
      const response = await fetch("http://localhost:8000/items");
      const data = await response.json();
      this.items = data;
    } catch (error) {
      console.error("API 호출 실패:", error);
    }
  }
};
</script>