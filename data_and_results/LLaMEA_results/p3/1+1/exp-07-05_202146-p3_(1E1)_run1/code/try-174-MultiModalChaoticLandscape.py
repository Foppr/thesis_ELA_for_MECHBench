import numpy as np

class MultiModalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Periodic components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Exponential decay terms with oscillatory modulation
        for i in range(self.dim):
            result += np.exp(-0.1 * np.abs(x[i])) * np.sin(5.0 * x[i])
            
        # Multi-scale trigonometric interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                
        # Chaotic sine-cosine coupling
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += np.sin(x[i] * np.cos(x[i]))
        result += 0.3 * np.sin(chaotic_sum) * np.cos(chaotic_sum)
        
        # High-frequency oscillatory noise
        for i in range(self.dim):
            result += 0.1 * np.sin(20.0 * x[i]) * np.cos(10.0 * x[i])
            
        # Multi-modal structure with basin boundaries
        for i in range(self.dim):
            result += 0.2 * np.sin(3.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional coupling with exponential weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.02 * (i + j))
                result += weight * x[i] * x[j] * np.sin(x[i] * x[j])
                
        # Asymmetric ruggedness
        for i in range(self.dim):
            result += 0.15 * np.sin(7.0 * x[i]) * np.cos(4.0 * x[i]) * np.exp(-0.03 * np.abs(x[i]))
            
        # Logarithmic penalty for distance from origin
        result += 0.05 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Multi-modal attractor terms
        attractor_sum = 0.0
        for i in range(self.dim):
            attractor_sum += np.sin(2.0 * x[i]) * np.cos(2.0 * x[i])
        result += 0.25 * np.sin(attractor_sum) * np.cos(attractor_sum)
        
        # Fractal-like self-similarity
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(1.5 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.01 * i)
        result += 0.1 * fractal
        
        return result