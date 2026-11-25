import numpy as np

class ChaoticRidgeLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial potential terms with chaotic coupling
        for i in range(self.dim):
            poly_term = (x[i]**5 + 0.7 * x[i]**4 + 0.3 * x[i]**3 + 0.15 * x[i]**2 + 0.05 * x[i])
            result += 0.3 * poly_term**2
        
        # Dynamic Gaussian ridge structures with chaotic frequency modulation
        for i in range(self.dim):
            ridge_sum = 0.0
            for j in range(1, 8):  # 7 different Gaussian components
                freq_mod = np.sin(0.3 * self.dim + j) * 0.3 + 0.7
                width = 0.4 + 0.1 * freq_mod * j
                height = 1.5 / (j * (j + 2))
                ridge_sum += height * np.exp(-0.5 * ((x[i] - j * freq_mod) / width)**2)
            result += 0.4 * ridge_sum**2
        
        # Chaotic cross-dimensional coupling with time-varying weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.sin(0.2 * (i + j) + self.dim) * 0.5 + 0.5
                coupling = (x[i]**3 + x[j]**3) * np.cos(weight * (x[i] - x[j]))
                result += 0.2 * coupling**2
        
        # Adaptive noise with chaotic amplitude scaling
        noise_scale = 0.15 + 0.08 * np.sin(self.dim * 0.7)
        for i in range(self.dim):
            noise = np.random.normal(0, noise_scale) if np.random.rand() < 0.4 else 0
            result += 0.12 * (x[i] + noise)**3
        
        # Dynamic conditioning based on chaotic gradient magnitude
        grad_magnitude = 0.0
        for i in range(self.dim):
            grad_magnitude += np.abs(5*x[i]**4 + 2.8*x[i]**3 + 0.9*x[i]**2 + 0.3*x[i] + 0.05)
        conditioning = 1.0 + 0.3 * np.tanh(grad_magnitude / self.dim) * np.sin(0.1 * self.dim)
        result *= conditioning
        
        # Multi-scale chaotic fractal structure with dynamic amplitude
        fractal_sum = 0.0
        for i in range(self.dim):
            for freq in [1, 3, 6, 12]:
                amp_mod = np.cos(0.2 * self.dim + freq) * 0.4 + 0.6
                fractal_sum += np.sin(freq * x[i]) * amp_mod * np.exp(-0.08 * (freq - 6)**2)
        result += 0.3 * fractal_sum**2
        
        # Chaotic ridge coupling with sinusoidal modulation
        chaos_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = np.sin(0.5 * (i + j) * self.dim) * 0.3 + 0.7
                chaos_coupling += np.cos(mod * x[i] * x[j]) * (x[i]**2 + x[j]**2)
        result += 0.18 * chaos_coupling**2
        
        # Final normalization and chaotic bias term
        result /= self.dim
        result += 0.03 * np.sum(np.abs(x)) * np.sin(0.1 * self.dim)
        
        return result