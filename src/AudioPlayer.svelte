<script context="module">
    import { onMount } from 'svelte'

    const players = new Set()
    
  
    export function stopAll() {
      players.forEach(p => p.pause())
    }
</script>

<script>
    
    let player
    export let src

    onMount(() => {
      // Like players.push(player)
    //   players.add(player)
      player.play()
    })
  
</script>

<style>
    audio {
        opacity: 0;
        position: absolute;
    }

</style>
  
<div>
    <audio
        bind:this={player}
        {src}
        controls>
        <track kind="captions" />
    </audio>
</div>
