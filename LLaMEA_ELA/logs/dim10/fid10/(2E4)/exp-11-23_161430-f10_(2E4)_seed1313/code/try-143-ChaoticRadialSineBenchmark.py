import numpy as np

class ChaoticRadialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic frequency and amplitude parameters for each dimension
        self.freqs = 2.0 + 3.0 * np.sin(np.arange(dim) * 1.7 + np.pi/5)
        self.amps = 1.5 + 2.5 * np.cos(np.arange(dim) * 1.9 + np.pi/7)
        # Adaptive radial basis widths controlled by chaotic sequences
        self.widths = 0.5 + 2.0 * np.sin(np.arange(dim) * 1.3 + np.pi/3)
        # Cross-dimensional coupling strengths with chaotic modulation
        self.couplings = 0.8 + 1.2 * np.cos(np.arange(dim) * 1.1 + np.pi/4)
        # Polynomial weights and exponents for higher-order interactions
        self.poly_weights = 2.0 + 1.5 * np.sin(np.arange(dim) * 1.2 + np.pi/6)
        self.exponents = 2.0 + 2.0 * np.cos(np.arange(dim) * 1.4 + np.pi/8)
        
    def f(self, x):
        # Ensure input is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis component with chaotic width variation
        radial = 0.0
        for i in range(self.dim):
            radial += np.exp(-0.5 * ((x[i] / self.widths[i])**2)) * \
                      np.sin(self.freqs[i] * x[i] + self.amps[i])
        
        # Sine-wave interaction component with multi-frequency coupling
        sine_interaction = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            amp = self.amps[i]
            sine_interaction += amp * np.sin(freq * x[i] + 0.5 * np.cos(freq * x[i]))
        
        # Cross-dimensional polynomial coupling with chaotic weights
        cross_poly = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            weight = self.couplings[i]
            poly_term = (x[i]**self.exponents[i] + x[j]**self.exponents[j])
            cross_poly += weight * poly_term * np.sin(0.3 * x[i] + 0.4 * x[j])
        
        # Chaotic polynomial component with adaptive exponents
        chaotic_poly = 0.0
        for i in range(self.dim):
            exponent = self.exponents[i]
            chaotic_poly += (x[i]**exponent + 2*x[i]**(exponent-1) - 3*x[i]**(exponent-2)) * \
                            np.cos(0.5 * x[i] + 0.3 * np.sin(x[i]))
        
        # Combined fitness with weighted components
        result = 0.4 * np.sum(x**2) + 0.3 * radial + 0.2 * sine_interaction + \
                 0.1 * cross_poly + 0.05 * chaotic_poly
        
        return result