<template>
  <h1>Vos messages</h1>
</template>
<script>
export default {
    data() {
        return {
        message,
        photo = true,
    }
},
    method: {
        showMessage() {
        this.message = message;
        if (unreadMessage > 1){
            return (this.message)
        }
        else{
            return false
        }

    },

},
}
</script>
