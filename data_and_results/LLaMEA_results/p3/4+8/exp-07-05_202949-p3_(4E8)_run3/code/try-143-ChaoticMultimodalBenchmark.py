import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic shifts and scaling
        self.chaotic_sequence = np.sin(np.arange(dim) * np.pi / 2.0) * 0.5 + 0.5
        # Additional chaotic sequence for frequency modulation
        self.freq_sequence = np.cos(np.arange(dim) * np.pi / 3.0) * 0.4 + 0.6
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic and polynomial terms with varying coefficients
        result = 0.0
        for i in range(self.dim):
            result += 0.7 * (x[i] - 1.3)**2 + 0.5 * (x[i] + 1.2)**2 + 0.02 * x[i]**4 + 0.006 * x[i]**6
        
        # Chaotic interaction terms with dynamic scaling and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_scale = 2.0 + 4.0 * self.chaotic_sequence[i] * self.chaotic_sequence[j]
                phase_shift = self.chaotic_sequence[i] * self.freq_sequence[j] * 0.5
                result += dynamic_scale * (x[i] - x[j])**2 * np.sin(5.0 * (x[i] + x[j]) + phase_shift)
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq1 = 3.0 + 2.0 * self.freq_sequence[i]
            freq2 = 4.0 + 2.5 * self.chaotic_sequence[i]
            amp1 = 1.0 + 0.3 * self.chaotic_sequence[i]
            amp2 = 0.6 + 0.4 * self.freq_sequence[i]
            result += amp1 * np.sin(freq1 * x[i] + self.chaotic_sequence[i]) * np.cos(freq2 * x[i]) + \
                      amp2 * np.sin(freq1 * x[i] + self.chaotic_sequence[i]**2) * np.cos(freq2 * x[i] + 0.6)
        
        # Add a global minimum shift based on chaotic sequence with non-linear transformation
        shift = np.array([self.chaotic_sequence[i] * 0.5 * np.sin(self.chaotic_sequence[i] * np.pi) for i in range(self.dim)])
        result += 0.2 * np.sum((x - shift)**2)
        
        # Add high-frequency noise to increase ruggedness with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(30.0 * x[i]) * np.cos(25.0 * x[i]) * (1.0 + 0.3 * self.chaotic_sequence[i] * self.freq_sequence[i])
        result += noise
        
        # Add complex polynomial term with mixed degrees and chaotic coefficients
        result += 0.003 * np.sum(x**3) + 0.0015 * np.sum(x**5) + 0.001 * np.sum(x**7) + 0.0007 * np.sum(x**9)
        
        # Add a chaotic perturbation term that varies with dimension
        perturbation = 0.0
        for i in range(self.dim):
            perturbation += 0.04 * np.sin(12.0 * x[i] + self.chaotic_sequence[i] * np.pi) * np.cos(10.0 * x[i] + self.freq_sequence[i] * np.pi)
        result += perturbation
        
        # Introduce additional multimodal component with enhanced chaotic modulation
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.06 * np.sin(20.0 * x[i] + self.chaotic_sequence[i] * np.pi) * np.cos(15.0 * x[i] + self.freq_sequence[i] * np.pi) + \
                          0.04 * np.sin(22.0 * x[i] + self.chaotic_sequence[i]**2) * np.cos(17.0 * x[i] + self.freq_sequence[i]**2)
        result += multimodal
        
        return result