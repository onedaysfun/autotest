// @ts-ignore
const { Typed } = window;

const typed2 = new Typed('#strike', {
  strings: [
    'hello',
    'hi',
    'hey',
    "g'day",
    'bonjour',
    'yo',
    'hola',
    'morning!',
    'hallo',
    'ciao',
    '&#128075;',
    'namaste',
    'hoi',
    "m'athchomaroon",
    'hiya',
    '袩褉懈胁械褌',
    'you got a sec?',
    '賲乇丨亘丕',
    'greetings!',
    'aloha',
    '銇撱倱銇仭銇�',
    'buenos dias',
    'nuqneH',
    'heya',
    'ol脿',
    'apipoula茂',
    'j0',
    'howdy',
    '砖诇讜诐',
    'yooooooooooo!',
    '浣犲ソ',
    '鍦ㄥ悧锛�',
    'you there?',
    'fraeslis',
    '鞐炒靹胳殧',
    'sul sul',
    'quick question...',
    'achuta',
    '啜膏à 啜膏⿳啜班﹢ 啜呧〞啜距ú',
    'ping',
    '围伪委蟻蔚蟿蔚',
    '爻賱丕賲',
  ],
  typeSpeed: 80,
  backSpeed: 60,
  smartBackspace: false,
  loop: true,
  shuffle: false,
  backDelay: 2000,
  startDelay: 3000,
});

// force the start of cursor animation while the `startDelay` is ticking
if (typed2.cursor != null) {
  // can't use `toggleBlinking(true)` here, as it has some extra checks
  // whether animation has started...which defeats the purpose
  typed2.cursor.classList.add('typed-cursor--blink');
}