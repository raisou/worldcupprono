import Store from '@/store'

export default {
  leaveBoard (board) {
    const modal = {
      obj: board,
      text: 'Etes vous sûr de vouloir quitter le tableau ' + board.name + ' ?',
      title: 'Quitter le tableau',
      variant: 'danger',
      action: 'leaveBoard'
    }
    Store.dispatch('displayConfirmationModal', { modal })
  },
  deleteBoard (board) {
    const modal = {
      obj: board,
      text: 'Etes vous sûr de vouloir supprimer le tableau ' + board.name + ' ?',
      title: 'Supprimer le tableau',
      variant: 'danger',
      action: 'deleteBoard'
    }
    Store.dispatch('displayConfirmationModal', { modal })
  }
}
