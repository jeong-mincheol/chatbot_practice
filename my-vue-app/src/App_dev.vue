<template>
  <div class="chat-container">
    <h2>Vue + FastAPI 챗봇</h2>

    <div class="chat-window">
      <div
        v-for="(msg, i) in messages"
        :key="i"
        class="chat-message"
        :class="{ user: msg.role === 'user', bot: msg.role === 'bot' }"
      >
        <div class="bubble">
          <b v-if="msg.role === 'user'">👤:</b>
          <b v-else>🤖:</b>
          {{ msg.text }}
        </div>
      </div>
    </div>

    <div class="input-area">
      <input
        v-model="input"
        @keyup.enter="sendMessage"
        placeholder="메시지를 입력하세요"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const input = ref('')
const messages = ref([])

const sendMessage = async () => {
  const text = input.value.trim()
  if (!text) return

  // 사용자 메시지 추가
  messages.value.push({ role: 'user', text })
  input.value = ''

  try {
    const res = await axios.post('http://127.0.0.1:8000/chat', { text })
    messages.value.push({ role: 'bot', text: res.data.response })
  } catch (err) {
    messages.value.push({ role: 'bot', text: '⚠️ 오류가 발생했어요.' })
    console.error(err)
  }
}
</script>

<style scoped>
.chat-container {
  max-width: 600px;
  margin: 2rem auto;
  font-family: 'Segoe UI', sans-serif;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 1rem;
  background-color: #fdfdfd;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
}

.chat-window {
  max-height: 400px;
  overflow-y: auto;
  padding: 0.5rem;
  margin-bottom: 1rem;
  background: #fafafa;
  border: 1px solid #eee;
  border-radius: 5px;
}

.chat-message {
  display: flex;
  margin: 0.5rem 0;
}

.chat-message.user {
  justify-content: flex-end;
}

.chat-message.bot {
  justify-content: flex-start;
}

.bubble {
  max-width: 70%;
  padding: 0.5rem 1rem;
  border-radius: 1rem;
  line-height: 1.4;
  background: #e0e0e0;
  color: #000;
  position: relative;
}

.chat-message.user .bubble {
  background: #aee1f9;
  color: #000;
}

.input-area input {
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  border-radius: 8px;
  border: 1px solid #ccc;
}
</style>
