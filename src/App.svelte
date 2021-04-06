<script>
	import AudioPlayer, { stopAll } from './AudioPlayer.svelte'
	import {fade} from 'svelte/transition'
	
	const carouselPhotos = [
		'https://picsum.photos/300/200?random=1',
		'https://picsum.photos/300/200?random=2',
		'https://picsum.photos/300/200?random=3'
	]
	let audioTracks = [
		'https://sveltejs.github.io/assets/music/strauss.mp3',
		'https://sveltejs.github.io/assets/music/holst.mp3',
		'https://sveltejs.github.io/assets/music/satie.mp3'
	]
	
	let index = 0
	
	const next = () => {
		console.log("NEXT")
		index = (index + 1) % carouselPhotos.length
	}
</script>

<style>
	img {
		position: fixed;
		width: auto;
		height: 100%;
	}
	.next-btn {
		width: 100%;
		height: 100%;
		position: fixed;
		opacity: 0;
	}
	.generate-btn {
		position: absolute;
		top: 95%;
		left:50%;
		/* width: 10%; */
		text-align: center;
		font-size: 28px;
		background-color: whitesmoke;
		opacity: 0.7;
	}
</style>

{#each [carouselPhotos[index]] as src (index)}
	<img transition:fade {src} alt="" />	
{/each}
<button class="next-btn" on:click={next}>Next!</button>

{#each [audioTracks[index]] as src (index)}
	<AudioPlayer {src} />
{/each}

<button class="generate-btn" on:click={()=>{}}>Generate</button>
