import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic shifts
        self.chaotic_sequence = np.sin(np.arange(dim) * np.pi / 3.0) * 0.5 + 0.5
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic and polynomial terms with higher-order interactions
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * (x[i] - 1.0)**2 + 0.3 * (x[i] + 1.0)**2 + 0.01 * x[i]**4
        
        # Enhanced chaotic interaction terms with dynamic scaling and multiple frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_scale = 1.0 + 3.0 * self.chaotic_sequence[i] * self.chaotic_sequence[j]
                result += dynamic_scale * (x[i] - x[j])**2 * np.sin(5.0 * (x[i] + x[j])) * np.cos(2.0 * (x[i] - x[j]))
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 1.2 * np.sin(3.0 * x[i] + self.chaotic_sequence[i]) * np.cos(2.0 * x[i]) + \
                      0.6 * np.sin(6.0 * x[i] + self.chaotic_sequence[i]**2) * np.cos(3.0 * x[i]) + \
                      0.3 * np.sin(9.0 * x[i] + self.chaotic_sequence[i]**3)
        
        # Add a global minimum shift based on chaotic sequence with non-linear transformation
        shift = np.array([self.chaotic_sequence[i] * 0.5 * np.sin(self.chaotic_sequence[i] * np.pi) for i in range(self.dim)])
        result += 0.15 * np.sum((x - shift)**2)
        
        # Add high-frequency noise to increase ruggedness with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(25.0 * x[i]) * np.cos(20.0 * x[i]) * (1.0 + 0.2 * self.chaotic_sequence[i]) * np.sin(5.0 * self.chaotic_sequence[i])
        result += noise
        
        # Add a complex polynomial term with mixed degrees and chaotic coefficients
        chaotic_coeffs = 0.001 * (1.0 + self.chaotic_sequence)
        result += np.sum(chaotic_coeffs * x**3) + 0.0005 * np.sum(x**5) + 0.0001 * np.sum(x**7)
        
        # Add a multi-modal component with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.2 * np.sin(10.0 * x[i]) * np.cos(8.0 * x[i]) + 0.1 * np.sin(15.0 * x[i])
        result += multimodal
        
        return result