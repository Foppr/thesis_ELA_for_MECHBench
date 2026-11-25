import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.oscillator_freq = 2.0
        self.fractal_hurst = 0.3
        self.saddle_strength = 1.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator potential
        quantum_potential = np.sum(0.5 * x**2 + 0.1 * np.sin(self.oscillator_freq * x))
        
        # Fractal Brownian motion component for ruggedness
        fbm_component = 0.0
        for i in range(self.dim):
            pos = x[i] / 5.0
            fbm_value = 0.0
            for k in range(1, 6):
                freq = 2**k
                amp = (2**(-k * self.fractal_hurst))
                fbm_value += amp * np.sin(freq * pos)
            fbm_component += fbm_value
        
        # Hyperbolic tangent saddle points with varying strength
        saddle_points = 0.0
        for i in range(self.dim):
            saddle_points += self.saddle_strength * (np.tanh(x[i])**2 - 1) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with cosine modulation
        coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling += 0.3 * np.cos(0.5 * x[i]) * np.sin(0.7 * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Polynomial chaos expansion component
        chaos_component = 0.0
        for i in range(self.dim):
            chaos_component += 0.4 * (x[i]**3 - 3*x[i]) * np.cos(0.8 * x[i])
        
        # Combine all components with adaptive weights based on dimensionality
        total = quantum_potential + 0.6 * fbm_component + 0.5 * saddle_points + 0.3 * coupling + 0.4 * chaos_component
        
        # Add a global scaling factor
        scaling = 1.0 + 0.1 * np.sin(self.dim * 0.2)
        
        return total * scaling