import numpy as np

class PolynomialChaosWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for polynomial chaos and wave interference
        self.poly_degrees = np.random.randint(3, 7, size=dim)
        self.wave_frequencies = np.random.uniform(1.5, 9.0, size=dim)
        self.stochastic_amplitudes = np.random.uniform(0.2, 2.5, size=dim)
        
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
            
        # Adaptive coupling between dimensions using polynomial terms
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x[i]**3 + x[i+1]**3) * np.exp(-0.15 * (x[i] - x[i+1])**2)
            
        # Stochastic perturbation component
        stochastic = 0.0
        for i in range(self.dim):
            stochastic += self.stochastic_amplitudes[i] * np.sin(x[i] + np.random.rand() * 2 * np.pi)
            
        # Multi-scale harmonic modulation with varying amplitudes and phases
        harmonic_modulation = 0.0
        for i in range(self.dim):
            harmonic_modulation += (np.sin(2.5 * self.wave_frequencies[i] * x[i]) + 
                                  0.6 * np.cos(3.5 * self.wave_frequencies[i] * x[i]) +
                                  0.4 * np.sin(4.5 * self.wave_frequencies[i] * x[i]))
            
        # Combined landscape with tunable weights
        return (0.9 * poly_chaos + 
                1.3 * wave_interference + 
                1.0 * coupling + 
                1.2 * stochastic + 
                0.8 * harmonic_modulation)