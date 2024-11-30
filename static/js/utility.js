//DOMが準備されたタイミングで実行される
$(function () {

  /**
   * ボタンHOVERイベントリスナー登録
   */
  $('.button').hover(
    /**
     * ボタンHOVER IN イベント処理
     */
    function () {
      // 要素にマウスを載せたらバックグラウンド色を変更
      $(this).css('background-color', 'red');
    },
    /**
     * ボタンHOVER OUT イベント処理
     */
    function () {
      // 要素からマウスをはなしたら元に戻す
      $(this).css('background-color', '');
    }
  );

});
