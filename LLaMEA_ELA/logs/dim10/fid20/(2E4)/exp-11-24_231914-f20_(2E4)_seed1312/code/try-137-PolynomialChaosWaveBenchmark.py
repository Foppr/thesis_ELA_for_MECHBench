import numpy as np

class PolynomialChaosWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for polynomial chaos and wave components
        self.poly_coeffs = np.random.uniform(0.5, 2.0, dim)
        self.wave_freqs = np.random.uniform(1.0, 8.0, dim)
        self.stochastic_amplitudes = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial chaos term with varying coefficients
        poly_chaos = np.sum(self.poly_coeffs * x**3 + 0.5 * x**4)
        
        # Trigonometric wave interference component
        wave_interference = 0.0
        for i in range(self.dim):
            freq = self.wave_freqs[i]
            wave_interference += (np.sin(freq * x[i]) * np.cos(freq * x[i]) +
                                0.5 * np.sin(2 * freq * x[i]) * np.cos(2 * freq * x[i]))
        
        # Stochastic perturbations with adaptive coupling
        stochastic_pert = 0.0
        for i in range(self.dim):
            amp = self.stochastic_amplitudes[i]
            stochastic_pert += amp * np.sin(x[i] + np.random.uniform(-0.5, 0.5)) * \
                              np.cos(0.3 * x[i] + np.random.uniform(-1.0, 1.0))
        
        # Multi-scale fractal-like structure with exponential decay
        fractal_structure = 0.0
        for i in range(self.dim):
            fractal_structure += (np.exp(-0.2 * x[i]**2) * 
                                np.sin(3 * x[i]) * 
                                np.cos(5 * x[i]) * 
                                np.sin(7 * x[i]))
        
        # Enhanced ruggedness through coupling of higher-order terms
        ruggedness = 0.0
        for i in range(self.dim - 1):
            ruggedness += (x[i]**5 + x[i+1]**5) * \
                         np.exp(-0.3 * (x[i] - x[i+1])**2) * \
                         np.sin(0.5 * (x[i] + x[i+1]))
        
        # Combined landscape with weighted components
        return 0.8 * poly_chaos + 1.5 * wave_interference + 1.2 * stochastic_pert + \
               1.0 * fractal_structure + 0.9 * ruggedness