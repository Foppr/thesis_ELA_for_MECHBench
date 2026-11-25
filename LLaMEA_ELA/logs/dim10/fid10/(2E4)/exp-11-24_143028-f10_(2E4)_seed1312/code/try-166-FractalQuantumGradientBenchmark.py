import numpy as np

class FractalQuantumGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters
        self.hurst = 0.3
        self.fractal_scale = 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component
        fbm_sum = 0.0
        for i in range(self.dim):
            # Simple fractal-like behavior using sine and cosine with varying frequencies
            fbm_sum += (np.sin(x[i]) * np.cos(2 * x[i]) + 
                       0.5 * np.sin(3 * x[i]) * np.cos(4 * x[i]) +
                       0.3 * np.sin(5 * x[i]) * np.cos(6 * x[i]))
        
        # Quantum harmonic oscillator component
        quantum_sum = 0.0
        for i in range(self.dim):
            # Harmonic oscillator potential with quantum-like modulation
            omega = 1.0 + 0.2 * np.sin(x[i])
            quantum_sum += 0.5 * omega**2 * x[i]**2 + 0.5 * (1 + 0.3 * np.cos(x[i]))
        
        # Adaptive gradient field component
        grad_sum = 0.0
        for i in range(self.dim):
            # Gradient field with adaptive strength based on position
            strength = 1.0 + 0.5 * np.sin(0.5 * x[i])
            grad_sum += strength * (x[i]**3 - 2*x[i]**2 + x[i])
        
        # Multi-scale interference patterns (modified interaction)
        interference_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced interaction range
                freq_i = 1.0 + 0.4 * np.sin(x[i])  # Increased frequency modulation
                freq_j = 1.0 + 0.4 * np.cos(x[j])  # Increased frequency modulation
                interference_sum += np.sin(freq_i * x[i]) * np.cos(freq_j * x[j]) * \
                                  np.exp(-0.15 * (x[i] - x[j])**2)  # Increased decay rate
        
        # Boundary attraction and repulsion
        boundary_sum = 0.0
        for i in range(self.dim):
            # Attract towards center, repel from boundaries with different strengths
            if x[i] < 0:
                boundary_sum += 2.0 * np.exp(-0.2 * (x[i] + 5.0)**2) * (1 + 0.2 * np.sin(4 * x[i]))
            else:
                boundary_sum += 1.5 * np.exp(-0.3 * (x[i] - 5.0)**2) * (1 + 0.1 * np.cos(3 * x[i]))
        
        # Chaotic modulation with logistic map (modified parameters)
        chaotic_sum = 0.0
        r = 3.9  # Slightly increased chaotic parameter for more complexity
        for i in range(self.dim):
            logistic_val = r * (x[i] / 5.0) * (1 - x[i] / 5.0)
            chaotic_sum += 0.5 * logistic_val**2  # Increased coefficient
        
        # Multi-modal Gaussian components with dynamic centers and widths
        gaussian_sum = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(x[i])  # Dynamic center
            width = 0.8 + 0.4 * np.cos(x[i])  # Dynamic width
            gaussian_sum += 1.5 * np.exp(-0.5 * ((x[i] - center) / width)**2)  # Increased amplitude
        
        # Final combined function
        result = fbm_sum + quantum_sum + grad_sum + interference_sum + boundary_sum + \
                 chaotic_sum + gaussian_sum
        
        return result