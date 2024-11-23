/**
 * ユーザー管理
 */

/**
 * 削除処理
 */
function deleteUser() {
  console.log('deleteUser');
  var id = $('input[name="user_id"]').val();

  var xhr = new XMLHttpRequest();
  var url = "http://127.0.0.1:5000/delete?user_id=" + id;
  xhr.open('DELETE', url);
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        // 削除成功、サーバーからのレスポンスを処理する
        const list = document.getElementById("user_list");
        list.innerHTML = xhr.response;
      } else if (xhr.status === 404) {
        // 削除失敗
        alert('削除するデータがありません。');
      } else {
        // 削除失敗
        const error = document.getElementById("error");
        error.innerHTML = xhr.response;
      }
    }
  };
  xhr.send();
}

/**
 * 一覧表示処理
 */
function getAllUser() {
  console.log('getAllUser');
  var xhr = new XMLHttpRequest();
  var url = "http://127.0.0.1:5000/get_all";
  xhr.open('GET', url);
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // サーバーからのレスポンスを表示する
      const list = document.getElementById("user_list");
      list.innerHTML = xhr.response;
    }
  };
  xhr.send();
}
