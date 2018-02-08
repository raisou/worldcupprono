function addAuthenticationHeader (token) {
  return {
    headers: { Authorization: `JWT ${token}` }
  }
}

export {addAuthenticationHeader}
