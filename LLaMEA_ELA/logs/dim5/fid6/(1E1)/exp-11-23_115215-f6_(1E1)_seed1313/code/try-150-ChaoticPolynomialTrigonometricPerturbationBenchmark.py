import numpy as np

class ChaoticPolynomialTrigonometricPerturbationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic and stochastic parameters
        self.chaotic_coefficients = np.random.uniform(0.1, 0.9, dim)
        self.wave_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.stochastic_coefficients = np.random.uniform(-0.3, 0.3, dim)
        self.coupling_weights = np.random.uniform(0.2, 1.0, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial with chaotic modulation
        base_poly = np.sum(x**4) * (1.0 + 0.2 * np.sin(np.sum(x) * 0.3))
        
        # Trigonometric wave components with chaotic frequencies
        trig_sum = 0.0
        for i in range(self.dim):
            freq = self.wave_frequencies[i] * (1.0 + 0.1 * np.sin(i * 0.5))
            trig_sum += 3.0 * np.sin(freq * x[i]) * \
                       np.cos(freq * x[i] * 0.8) + \
                       2.0 * np.sin(freq * x[i] * 1.5)
        
        # Chaotic polynomial coupling with dynamic weights
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = self.coupling_weights[i, j] * (1.0 + 0.3 * np.sin(i * 0.7))
                coupling_sum += weight * (x[i]**2 + x[j]**2) * \
                               np.exp(-0.3 * np.abs(x[i] - x[j]))
        
        # Stochastic perturbations with chaotic modulation
        stochastic_sum = 0.0
        for i in range(self.dim):
            stochastic_sum += self.stochastic_coefficients[i] * np.sin(x[i] * 12) * \
                            np.cos(x[i] * 9) + \
                            0.4 * np.random.uniform(-1, 1) * np.exp(-0.3 * x[i]**2)
        
        # Cross-dimensional chaotic interactions
        cross_sum = 0.0
        for i in range(self.dim):
            cross_sum += 0.5 * np.sin(x[i] * 3 + np.sum(x) * 0.15) * \
                       np.cos(x[i] * 2 + np.sum(x) * 0.08)
        
        # High-order chaotic terms
        high_order_sum = 0.0
        for i in range(self.dim):
            high_order_sum += 0.3 * (x[i]**6) + \
                            0.2 * np.sin(x[i]**4) * np.cos(x[i]**3)
        
        # Asymmetric chaotic coupling with dynamic weights
        asymmetric_sum = 0.0
        for i in range(1, self.dim):
            weight = 0.6 + 0.4 * np.sin(i * 0.4 + np.sum(x) * 0.05)
            asymmetric_sum += weight * (x[i] - x[i-1])**4
        
        # Chaotic global modulation
        global_mod = 0.7 * np.sin(np.sum(x**2) * 0.15) + \
                    0.4 * np.cos(np.prod(x)) + \
                    0.3 * np.sin(np.sum(np.abs(x))) + \
                    0.2 * np.tanh(np.sum(x**3))
        
        # Add chaotic perturbations to the base function
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += self.chaotic_coefficients[i] * \
                                  np.sin(x[i] * 15 + np.sum(x) * 0.2) * \
                                  np.cos(x[i] * 11)
        
        return base_poly + trig_sum + coupling_sum + stochastic_sum + \
               cross_sum + high_order_sum + asymmetric_sum + global_mod + chaotic_perturbation