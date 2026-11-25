import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic saddle-point component with logistic map dynamics
        chaotic_term = 0.0
        r = 3.8  # Slightly reduced chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x[-1]  # Periodic boundary
            else:
                x_prev = x[i-1]
            
            chaotic_term += np.sin(r * x_prev) * np.cos(x[i]) * np.exp(-0.12 * x[i]**2)
        
        # Embedded harmonic potentials with varying frequencies and amplitudes
        harmonic_term = 0.0
        for i in range(self.dim):
            freq = 1.2 + 0.4 * np.sin(0.5 * i)  # Slightly increased frequency modulation
            amp = 0.8 + 0.4 * np.cos(0.4 * i)   # Slightly decreased amplitude modulation
            harmonic_term += amp * (np.sin(freq * x[i]) ** 2) * np.exp(-0.06 * x[i]**2)
        
        # Cross-dimensional coupling with polynomial interaction terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (x[i] ** 2.5) * (x[j] ** 2.5) * np.exp(-0.15 * (x[i]**2 + x[j]**2))  # Changed exponents
        
        # Fractal coupling mechanism with recursive scaling
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 1.2 + 0.08 * np.sin(0.8 * i)  # Slightly increased scaling factor
            fractal_term += scale * np.sin(x[i] ** 2.5) * np.cos(x[i]) * np.exp(-0.03 * x[i]**2)  # Changed exponent
        
        # Gradient complexity modifier with adaptive noise
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(0.6 * x[i]) * np.cos(0.2 * x[i]) * (1.0 + 0.15 * np.random.rand())  # Increased frequency and noise
        
        # Global scaling factor based on solution distribution
        mean_x = np.mean(x)
        std_x = np.std(x)
        scale_factor = 1.0 + 0.25 * np.tanh(std_x - 1.2) + 0.12 * np.sin(mean_x)  # Slightly adjusted parameters
        
        return (chaotic_term + harmonic_term + coupling_term + fractal_term + noise) * scale_factor