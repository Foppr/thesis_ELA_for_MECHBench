import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequences for dynamic shifts and scaling
        self.chaotic_sequence = np.sin(np.arange(dim) * np.pi / 3.0) * 0.5 + 0.5
        self.freq_sequence = np.cos(np.arange(dim) * np.pi / 2.5) * 0.3 + 0.7
        self.phase_sequence = np.tan(np.arange(dim) * np.pi / 4.0) * 0.2 + 0.8
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic and polynomial terms with varying coefficients
        result = 0.0
        for i in range(self.dim):
            result += 0.6 * (x[i] - 1.2)**2 + 0.4 * (x[i] + 1.1)**2 + 0.015 * x[i]**4 + 0.005 * x[i]**6
        
        # Chaotic interaction terms with dynamic scaling and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_scale = 1.5 + 3.0 * self.chaotic_sequence[i] * self.chaotic_sequence[j]
                phase_shift = self.chaotic_sequence[i] * self.phase_sequence[j]
                result += dynamic_scale * (x[i] - x[j])**2 * np.sin(4.0 * (x[i] + x[j]) + phase_shift)
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq1 = 2.5 + 1.5 * self.freq_sequence[i]
            freq2 = 3.5 + 2.0 * self.chaotic_sequence[i]
            amp1 = 0.9 + 0.2 * self.chaotic_sequence[i]
            amp2 = 0.5 + 0.3 * self.freq_sequence[i]
            result += amp1 * np.sin(freq1 * x[i] + self.chaotic_sequence[i]) * np.cos(freq2 * x[i]) + \
                      amp2 * np.sin(freq1 * x[i] + self.chaotic_sequence[i]**2) * np.cos(freq2 * x[i] + 0.5)
        
        # Add a global minimum shift based on chaotic sequence with non-linear transformation
        shift = np.array([self.chaotic_sequence[i] * 0.4 * np.sin(self.chaotic_sequence[i] * np.pi) for i in range(self.dim)])
        result += 0.15 * np.sum((x - shift)**2)
        
        # Add high-frequency noise to increase ruggedness with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.08 * np.sin(25.0 * x[i]) * np.cos(20.0 * x[i]) * (1.0 + 0.2 * self.chaotic_sequence[i] * self.freq_sequence[i])
        result += noise
        
        # Add complex polynomial term with mixed degrees and chaotic coefficients
        result += 0.002 * np.sum(x**3) + 0.001 * np.sum(x**5) + 0.0008 * np.sum(x**7) + 0.0005 * np.sum(x**9)
        
        # Add a chaotic perturbation term that varies with dimension
        perturbation = 0.0
        for i in range(self.dim):
            perturbation += 0.03 * np.sin(10.0 * x[i] + self.chaotic_sequence[i] * np.pi) * np.cos(8.0 * x[i] + self.phase_sequence[i] * np.pi)
        result += perturbation
        
        # Add improved chaotic modulation with enhanced ruggedness
        for i in range(self.dim):
            result += 0.02 * np.sin(30.0 * x[i] + self.chaotic_sequence[i] * np.pi) * np.cos(25.0 * x[i] + self.phase_sequence[i] * np.pi) * (1.0 + 0.1 * self.freq_sequence[i])
        
        # Add a new multimodal component with adaptive chaotic scaling
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.05 * (np.sin(5.0 * x[i] + self.chaotic_sequence[i] * np.pi) + 
                                 np.cos(3.0 * x[i] + self.freq_sequence[i] * np.pi)) * \
                          (1.0 + 0.15 * self.chaotic_sequence[i] * self.freq_sequence[i])
        result += multimodal
        
        # Add new chaotic interaction term with higher-order polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.01 * (x[i]**3 - x[j]**3) * np.sin(5.0 * (x[i] + x[j]) + self.chaotic_sequence[i] * self.chaotic_sequence[j])
        
        # Add adaptive noise scaling based on dimensionality
        adaptive_noise = 0.0
        for i in range(self.dim):
            adaptive_noise += 0.02 * np.sin(15.0 * x[i]) * np.cos(12.0 * x[i]) * (1.0 + 0.3 * self.chaotic_sequence[i] * self.freq_sequence[i] * self.phase_sequence[i])
        result += adaptive_noise
        
        # Add enhanced multimodal component with dynamic amplitude modulation
        enhanced_multimodal = 0.0
        for i in range(self.dim):
            amp_mod = 0.1 + 0.05 * self.chaotic_sequence[i] * self.freq_sequence[i]
            enhanced_multimodal += amp_mod * (np.sin(7.0 * x[i] + self.chaotic_sequence[i] * np.pi) + 
                                              np.cos(4.0 * x[i] + self.freq_sequence[i] * np.pi)) * \
                                  (1.0 + 0.2 * self.chaotic_sequence[i] + 0.1 * self.freq_sequence[i])
        result += enhanced_multimodal
        
        return result