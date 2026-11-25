import numpy as np

class PolynomialTrigonometricPerturbationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wave frequencies and stochastic parameters
        self.wave_frequencies = np.linspace(0.5, 3.0, dim)
        self.stochastic_params = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with trigonometric modulation
        f_val = np.sum(x**4) * (1.0 + 0.3 * np.cos(np.sum(x) * 0.2))
        
        # Trigonometric wave components with varying amplitudes and phases
        for i in range(self.dim):
            f_val += 0.7 * np.sin(self.wave_frequencies[i] * x[i] + i * 0.5) * \
                     np.cos(self.wave_frequencies[i] * x[i] * 0.8) + \
                     0.4 * np.sin(self.wave_frequencies[i] * x[i] * 1.5)
        
        # Polynomial interactions with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                interaction = np.exp(-0.2 * (j - i)) * (x[i]**2 + x[j]**2)
                f_val += 0.3 * interaction * np.sin(x[i] * x[j])
        
        # Stochastic perturbations with dynamic scaling
        for i in range(self.dim):
            stochastic_pert = self.stochastic_params[i] * np.random.normal(0, 1) * \
                              (1.0 + 0.2 * np.sin(i * 0.3))
            f_val += 0.25 * x[i]**3 * stochastic_pert
        
        # Cross-dimensional coupling with hyperbolic functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i == 0:
                    coupling = np.tanh(x[j] - x[i])
                else:
                    coupling = np.tanh((x[j] - x[i]) * (i + 1))
                f_val += 0.15 * coupling * (x[i]**2 + x[j]**2)
        
        # Asymmetric polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            asym_term = x[i]**5 + 0.3 * np.sin(x[i]) * x[i]**2
            f_val += 0.2 * asym_term * (1.0 + 0.1 * np.cos(i * 0.4))
        
        # Global correlation through multi-wave interaction
        f_val += 0.3 * np.sin(np.sum(np.sin(x)) * 0.5) + \
                 0.2 * np.cos(np.sum(np.cos(x)) * 0.3) + \
                 0.1 * np.tan(np.sum(np.abs(x)) * 0.1)
        
        # Add noise with dimension-dependent intensity
        noise = np.random.normal(0, 0.01, self.dim)
        f_val += np.sum(noise * x)
        
        return f_val