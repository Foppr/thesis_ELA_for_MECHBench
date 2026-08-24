import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic shifts and scaling
        self.chaotic_sequence = np.sin(np.arange(dim) * np.pi / 3.0) * 0.5 + 0.5
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic and polynomial terms with adaptive coefficients
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * (x[i] - 1.0)**2 + 0.3 * (x[i] + 1.0)**2 + 0.01 * x[i]**4
        
        # Enhanced chaotic interaction terms with dynamic scaling and coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_scale = 1.0 + 2.5 * self.chaotic_sequence[i] * self.chaotic_sequence[j]
                coupling = np.sin(3.0 * (x[i] - x[j])) * np.cos(2.0 * (x[i] + x[j]))
                result += dynamic_scale * (x[i] - x[j])**2 * coupling
        
        # Add chaotic sinusoidal components with varying frequencies and adaptive amplitudes
        for i in range(self.dim):
            amplitude = 1.0 + 0.3 * self.chaotic_sequence[i]
            result += amplitude * np.sin(3.0 * x[i] + self.chaotic_sequence[i]) * np.cos(1.5 * x[i]) + \
                      0.4 * np.sin(6.0 * x[i] + self.chaotic_sequence[i]**2) * np.cos(3.0 * x[i])
        
        # Add a global minimum shift based on chaotic sequence with non-linear scaling
        shift = np.array([self.chaotic_sequence[i] * 0.5 for i in range(self.dim)])
        result += 0.2 * np.sum((x - shift)**2)
        
        # Add high-frequency noise with adaptive scaling to increase ruggedness
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(30.0 * x[i]) * np.cos(25.0 * x[i]) * (1.0 + 0.2 * self.chaotic_sequence[i])
        result += noise
        
        # Add complex polynomial terms with mixed degrees and chaotic modulation
        result += 0.002 * np.sum(x**3) + 0.001 * np.sum(x**5) + 0.0005 * np.sum(x**7)
        
        # Add a chaotic coupling term between all variables with dynamic modulation
        chaotic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling += (x[i] * x[j]) * np.sin(2.0 * self.chaotic_sequence[i] * self.chaotic_sequence[j])
        result += 0.05 * chaotic_coupling
        
        return result