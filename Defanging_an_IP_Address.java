class Solution {
    public String defangIPaddr(String address) {
        
       List<String> ip=Arrays.asList(address);
		List<String> result=ip.stream().filter(c -> c.contains(".")).map(c -> c.replace(".", "[.]")).collect(Collectors.toList());
		return result.get(0);
    }
}