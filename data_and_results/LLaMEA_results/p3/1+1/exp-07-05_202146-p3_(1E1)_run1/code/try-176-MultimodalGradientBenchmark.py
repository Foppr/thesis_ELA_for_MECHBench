import numpy as np

class MultimodalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coeffs = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * 0.5)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            result += amp * np.sin(freq * x[i] + self.phase_shifts[i]) * np.cos(freq * x[i] + self.phase_shifts[i] * 0.7)
            
        # Polynomial interaction terms with mixed degrees
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * x[i]**3 * x[j]**2 * np.sin(x[i] + x[j])
                
        # Gradient-based basin structure with varying steepness
        for i in range(self.dim):
            result += 0.2 * np.abs(x[i])**1.5 * np.sin(3.0 * x[i])
            
        # Multi-scale oscillatory component with exponential decay
        for i in range(self.dim):
            result += 0.15 * np.sin(10.0 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Cross-dimensional coupling with dynamic weights
        coupling_sum = 0.0
        for i in range(self.dim):
            coupling_sum += x[i] * np.sin(x[i] * self.coeffs[i])
        result += 0.25 * coupling_sum**2
            
        # Asymmetric multimodal structure with varying peak heights
        for i in range(self.dim):
            peak_height = 1.0 + 0.8 * np.sin(i * 0.4)
            result += peak_height * np.sin(5.0 * x[i])**2 * np.cos(2.0 * x[i])**2
            
        # Non-separable high-order interaction with varying influence
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.05 * x[i]**2 * x[j] * x[k] * np.cos(x[i] + x[j] + x[k])
                    
        # Add a global minimum attractor with logarithmic penalty
        result += 0.1 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Enhanced noise component with chaotic-like behavior
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(7.0 * x[i] + i * 0.2) * np.cos(4.0 * x[i] + i * 0.3)
        result += noise
        
        # Fractal-like scaling with recursive structure
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2.0 * x[i]) * np.cos(1.0 * x[i]) * np.sin(0.5 * x[i])
        result += 0.08 * fractal**3
        
        return result