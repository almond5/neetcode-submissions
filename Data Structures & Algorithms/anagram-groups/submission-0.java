class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> mapper = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            String original = strs[i];
            char[] charArray = original.toCharArray();
            Arrays.sort(charArray);
            var value = mapper.getOrDefault(new String(charArray), null);
            if (value != null) {
                value.add(strs[i]);
                mapper.put(new String(charArray), value);
            } else {
                List<String> innerString = new ArrayList<>();
                innerString.add(strs[i]);
                mapper.put(new String(charArray), innerString);
            }
        }

        List<List<String>> result = new ArrayList<>(mapper.values());
        return result;
    }
}
