import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic and cubic terms with irrational scaling factors
        result = 0.0
        for i in range(self.dim):
            irrational_scale = np.sqrt(2) + np.pi * 0.1
            result += irrational_scale * (x[i]**2 + 0.5 * x[i]**3) + 0.01 * x[i]**4
        
        # Add chaotic interaction terms using golden ratio and Fibonacci-like coupling
        phi = (1 + np.sqrt(5)) / 2
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = int(phi * (i + j)) % 7
                result += (0.5 + 0.1 * coupling) * np.sin(2 * np.pi * (x[i] - x[j]))**2
        
        # Introduce fractal-like structure using sine and cosine with irrational frequencies
        for i in range(self.dim):
            result += np.sin(np.pi * x[i] * np.e) * np.cos(np.pi * x[i] * np.sqrt(3)) + \
                      0.3 * np.sin(2 * np.pi * x[i] * np.sqrt(7)) * np.cos(2 * np.pi * x[i] * np.sqrt(5))
        
        # Add non-uniform scaling with logarithmic components
        for i in range(self.dim):
            result += 0.05 * np.log(1 + np.abs(x[i])) * x[i]**2
        
        # Include a highly irregular periodic component with prime-based frequencies
        periodic = 0.0
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i in range(self.dim):
            freq = primes[i % len(primes)]
            periodic += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        result += 0.2 * periodic
        
        # Add a noise-like term with chaotic behavior using logistic map
        noise = 0.0
        r = 3.99
        for i in range(self.dim):
            logistic = 0.5
            for _ in range(10):
                logistic = r * logistic * (1 - logistic)
            noise += 0.03 * logistic * np.sin(10 * x[i])
        result += noise
        
        # Shift global minimum with a complex offset
        result += 0.1 * np.sum(np.sin(0.1 * x)**2) + 0.05 * np.sum(np.cos(0.2 * x)**2)
        
        return result