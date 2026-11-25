import numpy as np

class PolynomialChaosWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for polynomial chaos and wave interference
        self.poly_degrees = np.random.randint(3, 15, size=dim)
        self.wave_frequencies = np.random.uniform(1.0, 20.0, size=dim)
        self.stochastic_amplitudes = np.random.uniform(0.1, 5.0, size=dim)
        # Add fractal coupling weights
        self.fractal_weights = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Additional nonlinearity parameters
        self.nonlinear_weights = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with varying degrees and additional nonlinearity
        poly_chaos = 0.0
        for i in range(self.dim):
            degree = self.poly_degrees[i]
            poly_chaos += (x[i]**degree) * np.sin(self.wave_frequencies[i] * x[i]) * self.nonlinear_weights[i]
            
        # Trigonometric wave interference pattern with enhanced coupling
        wave_interference = 0.0
        for i in range(self.dim):
            freq = self.wave_frequencies[i]
            wave_interference += np.cos(freq * x[i]) * np.sin(freq * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Fractal-like adaptive coupling between dimensions with enhanced nonlinearity
        coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += self.fractal_weights[i, j] * np.sin(3 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.15 * (x[i] - x[j])**2)
            
        # Stochastic perturbation component with dynamic phase and additional noise
        stochastic = 0.0
        for i in range(self.dim):
            stochastic += self.stochastic_amplitudes[i] * np.sin(x[i] + np.random.rand() * 2 * np.pi + 0.1 * x[(i+1)%self.dim]) + \
                         0.5 * np.random.randn() * np.cos(0.3 * x[i]) + \
                         0.2 * np.sin(5 * x[i]) * np.cos(2 * x[i])
            
        # Multi-scale harmonic modulation with varying amplitudes and phases
        harmonic_modulation = 0.0
        for i in range(self.dim):
            harmonic_modulation += (np.sin(3 * self.wave_frequencies[i] * x[i]) + 
                                  0.6 * np.cos(4 * self.wave_frequencies[i] * x[i]) +
                                  0.4 * np.sin(5 * self.wave_frequencies[i] * x[i]) +
                                  0.2 * np.cos(6 * self.wave_frequencies[i] * x[i]))
            
        # Add fractal-like exponential term for increased ruggedness with additional nonlinearity
        fractal_ruggedness = 0.0
        for i in range(self.dim):
            fractal_ruggedness += np.exp(-0.4 * (x[i] - np.mean(x))**2) * np.sin(20 * x[i]) + \
                                 0.3 * np.sin(10 * x[i]) * np.cos(5 * x[i]) + \
                                 0.1 * np.tanh(2 * x[i])
            
        # Combined landscape with tunable weights optimized for better fitness
        return (1.1 * poly_chaos + 
                1.5 * wave_interference + 
                1.2 * coupling + 
                1.4 * stochastic + 
                0.9 * harmonic_modulation + 
                0.7 * fractal_ruggedness)