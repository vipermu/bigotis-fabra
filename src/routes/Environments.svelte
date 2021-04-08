<script>
	// import AudioPlayer, { stopAll } from "./components/AudioPlayer.svelte";
	import { fade } from "svelte/transition";
	import { onMount } from "svelte";

	let index = 0;
	let numWords = 0;

	let elapsedArray = [];

	onMount(async () => {
		const res = await fetch(`${serverUrl}/generate_environments`);
		const response = await res.json();
		numWords = response["numWords"];
	});

	const beginning = new Date();
	let beginningTime = beginning.getTime();

	const getElapsedTime = () => {
		let current = new Date();
		let currentTime = current.getTime();

		let elapsedTime = currentTime - beginningTime;
		beginningTime = currentTime;

		return elapsedTime / 1000;
	};

	let audioTracks = [
		"https://sveltejs.github.io/assets/music/strauss.mp3",
		"https://sveltejs.github.io/assets/music/holst.mp3",
		"https://sveltejs.github.io/assets/music/satie.mp3",
	];

	const next = () => {
		index = (index + 1) % numWords;

		let elapsedTime = getElapsedTime();
		elapsedArray.push(elapsedTime);

		console.log("Index", index);
		console.log("Elapsed Time", elapsedTime);
	};

	const generate = async () => {
		console.log("Generating Image...");

		const elapsedTimesArg = `elapsedTimes=${elapsedArray.join(",")}`;
		console.log("ELAPSED TIMES ARG", elapsedTimesArg);

		const res = await fetch(
			`${serverUrl}/generate_img_from_times?${elapsedTimesArg}`
		);
		const response = await res.json();

		const prompt = response["prompt"];
		index = prompt;
	};

	const serverUrl = "http://127.0.0.1:8000";
</script>

<img transition:fade src={`/environments/img/${index}.png`} alt="" />
<button class="next-btn" on:click={next}>Next!</button>

<button class="generate-btn" on:click={generate}>Generate</button>

<style>
	img {
		position: fixed;
		width: 100%;
		height: 100%;
		display: block;
		margin-left: auto;
		margin-right: auto;
	}
	.next-btn {
		width: 100%;
		height: 100%;
		position: fixed;
		opacity: 0;
	}
	.generate-btn {
		position: absolute;
		top: 85%;
		left: 50%;
		margin-left: -50pt;
		width: 100pt;
		text-align: center;
		font-size: 28px;
		background-color: whitesmoke;
		opacity: 0.7;
	}
</style>
