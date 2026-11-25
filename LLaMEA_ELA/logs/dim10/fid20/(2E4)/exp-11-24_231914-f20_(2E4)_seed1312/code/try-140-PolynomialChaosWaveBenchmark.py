import numpy as np

class PolynomialChaosWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for polynomial chaos and wave interference
        self.poly_degrees = np.random.randint(3, 10, size=dim)
        self.wave_frequencies = np.random.uniform(1.0, 12.0, size=dim)
        self.stochastic_amplitudes = np.random.uniform(0.1, 3.0, size=dim)
        # Add fractal coupling weights
        self.fractal_weights = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with varying degrees
        poly_chaos = 0.0
        for i in range(self.dim):
            degree = self.poly_degrees[i]
            poly_chaos += (x[i]**degree) * np.sin(self.wave_frequencies[i] * x[i])
            
        # Trigonometric wave interference pattern
        wave_interference = 0.0
        for i in range(self.dim):
            freq = self.wave_frequencies[i]
            wave_interference += np.cos(freq * x[i]) * np.sin(freq * x[i])
            
        # Fractal-like adaptive coupling between dimensions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += self.fractal_weights[i, j] * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
            
        # Stochastic perturbation component with dynamic phase
        stochastic = 0.0
        for i in range(self.dim):
            stochastic += self.stochastic_amplitudes[i] * np.sin(x[i] + np.random.rand() * 2 * np.pi + 0.1 * x[(i+1)%self.dim])
            
        # Multi-scale harmonic modulation with varying amplitudes and phases
        harmonic_modulation = 0.0
        for i in range(self.dim):
            harmonic_modulation += (np.sin(2 * self.wave_frequencies[i] * x[i]) + 
                                  0.5 * np.cos(3 * self.wave_frequencies[i] * x[i]) +
                                  0.3 * np.sin(4 * self.wave_frequencies[i] * x[i]) +
                                  0.1 * np.cos(5 * self.wave_frequencies[i] * x[i]))
            
        # Add fractal-like exponential term for increased ruggedness
        fractal_ruggedness = 0.0
        for i in range(self.dim):
            fractal_ruggedness += np.exp(-0.5 * (x[i] - np.mean(x))**2) * np.sin(10 * x[i])
            
        # Combined landscape with tunable weights
        return (0.8 * poly_chaos + 
                1.2 * wave_interference + 
                0.9 * coupling + 
                1.1 * stochastic + 
                0.7 * harmonic_modulation + 
                0.5 * fractal_ruggedness)