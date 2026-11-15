import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic shifts
        self.chaotic_sequence = np.sin(np.arange(dim) * np.pi / 4.0) * 0.5 + 0.5
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic terms with varying scales
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - 1.0)**2 + (x[i] + 1.0)**2
        
        # Add polynomial interaction terms with chaotic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use chaotic scaling factor for interaction strength
                scale_factor = self.chaotic_sequence[i] * self.chaotic_sequence[j] * 2.0 + 1.0
                result += scale_factor * (x[i] - x[j])**2
        
        # Add sinusoidal modulation with chaotic frequencies
        for i in range(self.dim):
            freq = 2.0 + self.chaotic_sequence[i] * 3.0
            result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Add higher-order polynomial terms for increased curvature
        result += 0.01 * np.sum(x**4) + 0.001 * np.sum(x**8)
        
        # Add chaotic global minimum shift
        shift = np.array([np.sin(i * np.pi / 3.0) * 0.8 for i in range(self.dim)])
        result += 0.3 * np.sum((x - shift)**2)
        
        # Add chaotic periodic component for ruggedness
        periodic = 0.0
        for i in range(self.dim):
            freq1 = 3.0 + self.chaotic_sequence[i] * 2.0
            freq2 = 5.0 + self.chaotic_sequence[i] * 3.0
            periodic += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
        result += 0.2 * periodic
        
        # Add noise-like chaotic component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(15.0 * x[i] + self.chaotic_sequence[i] * np.pi) * np.cos(12.0 * x[i])
        result += noise
        
        return result