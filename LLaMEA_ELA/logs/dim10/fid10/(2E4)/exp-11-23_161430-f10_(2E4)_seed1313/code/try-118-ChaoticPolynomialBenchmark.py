import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Adaptive parameters for chaotic behavior
        self.freqs = 2.0 + 3.0 * np.sin(np.arange(dim) * 0.5 + 1.0)
        self.amps = 1.0 + 2.0 * np.cos(np.arange(dim) * 0.7 + 0.5)
        self.powers = 3.0 + 2.0 * np.sin(np.arange(dim) * 0.9 + 0.3)
        self.coupling_strengths = 0.5 + 1.5 * np.cos(np.arange(dim) * 0.6 + 0.8)
        self.modulators = 0.2 + 0.8 * np.sin(np.arange(dim) * 1.1 + 0.4)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component
        chaotic_sine = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            amp = self.amps[i]
            chaotic_sine += amp * np.sin(freq * x[i] + np.sin(x[i]**2)) * \
                            np.cos(0.5 * x[i] + np.cos(x[i]))
        
        # Polynomial potential with variable exponents
        poly_potential = 0.0
        for i in range(self.dim):
            power = self.powers[i]
            poly_potential += (x[i]**power + 0.5 * x[i]**(power-1) - 2*x[i]**2 + x[i]) * \
                              np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with adaptive strength
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            strength = self.coupling_strengths[i]
            cross_coupling += strength * np.sin(x[i] + x[j]) * \
                              np.cos(0.3 * x[i] * x[j] + np.sin(x[i])) * \
                              np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Modulated chaotic interaction
        modulated_interaction = 0.0
        for i in range(self.dim):
            mod = self.modulators[i]
            interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    interaction += np.sin(x[i] * x[j] + mod * np.cos(x[i])) * \
                                   np.exp(-0.1 * (x[i] - x[j])**2)
            modulated_interaction += interaction
        
        # Combine all components
        result = 0.3 * chaotic_sine + 0.4 * poly_potential + 0.2 * cross_coupling + 0.1 * modulated_interaction
        
        return result