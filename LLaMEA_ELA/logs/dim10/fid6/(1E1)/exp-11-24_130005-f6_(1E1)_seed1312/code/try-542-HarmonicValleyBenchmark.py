import numpy as np

class HarmonicValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial harmonic component with periodic modulations
        radial_harmonic = 0.0
        r = np.sqrt(np.sum(x_scaled**2))
        
        # Multiple sinusoidal harmonics with varying frequencies and amplitudes
        for i in range(1, min(6, self.dim + 1)):
            freq = i * 2.0 + 0.5 * np.sin(i * 0.7)
            amp = 1.5 + 0.8 * np.cos(i * 0.9)
            radial_harmonic += amp * np.sin(freq * r) * np.exp(-0.5 * r**2)
        
        # Multi-dimensional periodic structure with interaction terms
        periodic_structure = 0.0
        for i in range(self.dim):
            # Periodic components with phase shifts
            phase = 0.5 * np.sin(i * 0.8) + 0.3 * np.cos(i * 0.6)
            periodic_structure += np.sin(x_scaled[i] * 3.0 + phase)**2 + \
                                np.cos(x_scaled[i] * 2.5 + phase)**2
            
        # Exponentially decaying harmonic interactions between dimensions
        interactions = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Distance-based exponential decay with harmonic modulation
                dist = np.abs(x_scaled[i] - x_scaled[j])
                weight = 2.0 * np.exp(-dist**2)
                interaction = np.sin(2.0 * (x_scaled[i] + x_scaled[j])) * \
                             np.cos(1.5 * (x_scaled[i] - x_scaled[j]))
                interactions += weight * interaction
        
        # Central attractive force with radial dependence
        central_force = 0.0
        for i in range(self.dim):
            # Exponential decay towards center with sinusoidal modulation
            dist_to_center = np.abs(x_scaled[i])
            central_force += np.exp(-dist_to_center**2) * np.sin(3.0 * x_scaled[i])
        
        # Combine all components with modified weights
        return 1.5 * radial_harmonic + 0.8 * periodic_structure + 1.2 * interactions + 0.9 * central_force