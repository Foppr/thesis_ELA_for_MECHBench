import numpy as np

class PeriodicBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial periodic component with multiple frequency harmonics
        radial_periodic = 0.0
        for i in range(self.dim):
            # Radial distance from origin
            r = np.sqrt(np.sum(x_scaled[:i+1]**2)) if i < self.dim - 1 else np.abs(x_scaled[i])
            # Multiple harmonic frequencies
            freqs = [1.0, 2.0, 3.0, 4.0]
            for freq in freqs:
                radial_periodic += np.sin(freq * r) * np.cos(freq * r) * np.exp(-0.5 * r**2)
        
        # Multi-scale trigonometric interactions with exponential barriers
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance between dimensions
                dist = np.abs(x_scaled[i] - x_scaled[j])
                # Exponential barrier effect
                barrier = np.exp(-dist**2 / 0.5)
                # Trigonometric interaction with varying frequencies
                trig_interaction += barrier * np.sin(3.0 * (x_scaled[i] + x_scaled[j])) * \
                                  np.cos(2.0 * (x_scaled[i] - x_scaled[j]))
        
        # Symmetric radial polynomial landscape with chaotic modulation
        radial_poly = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x_scaled[:i+1]**2)) if i < self.dim - 1 else np.abs(x_scaled[i])
            # Polynomial terms with chaotic coefficients
            coeff = 1.0 + 0.3 * np.sin(i * 1.7)
            radial_poly += coeff * r**4 + 0.5 * r**6
        
        # Exponential sharp peak regions with periodic positioning
        peaks = 0.0
        for i in range(self.dim):
            # Periodic peak positions
            peak_pos = np.sin(i * 1.3) * 0.8
            # Sharp exponential peak
            peaks += 5.0 * np.exp(-10.0 * (x_scaled[i] - peak_pos)**2)
        
        # Cross-dimensional coupling with sinusoidal phase relationships
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Phase-shifted interaction
                phase = np.sin(0.5 * x_scaled[i] + 0.3 * x_scaled[j])
                coupling += phase * (x_scaled[i]**2 + x_scaled[j]**2) * \
                           np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Global scaling and combination of components
        return 1.5 * radial_periodic + 1.2 * trig_interaction + 0.8 * radial_poly + 1.0 * peaks + 0.9 * coupling