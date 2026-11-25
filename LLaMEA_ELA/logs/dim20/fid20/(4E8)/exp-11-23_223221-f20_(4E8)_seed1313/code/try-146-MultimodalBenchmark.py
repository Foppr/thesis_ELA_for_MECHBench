import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic trigonometric base with adaptive frequency and amplitude
        trig_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.7 * x[i])
            amp = 1.0 + 0.5 * np.cos(0.9 * x[i])
            trig_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Elliptic shaping with dynamic eccentricity and rotation
        elliptic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                eccentricity = 1.0 + 0.3 * np.sin(0.5 * x[i])
                angle = 0.2 * np.cos(0.6 * x[j])
                diff_i = x[i] * np.cos(angle) - x[j] * np.sin(angle)
                diff_j = x[i] * np.sin(angle) + x[j] * np.cos(angle)
                elliptic_term += (diff_i**2 / eccentricity + diff_j**2 * eccentricity) / 2.0
        
        # Dynamic coupling with time-varying weights and phase shifts
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.3 * np.sin(0.4 * x[i] + 0.6 * x[j])
                phase = 0.3 * np.cos(0.5 * x[i] - 0.7 * x[j])
                coupling_term += weight * np.sin(x[i] * x[j] + phase) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Stochastic perturbation with adaptive noise intensity
        noise_term = 0.0
        for i in range(self.dim):
            noise_intensity = 0.2 + 0.1 * np.abs(x[i])
            noise_term += noise_intensity * (np.random.rand() - 0.5) * np.sin(10 * x[i])
        
        # Multi-scale harmonic modulation with varying amplitudes and frequencies
        harmonic_term = 0.0
        for i in range(self.dim):
            scales = [1.0, 2.0, 3.0, 4.0]
            for s in scales:
                harmonic_term += 0.1 * np.sin(s * x[i]) * np.cos(s * x[i] + 0.5 * np.sin(x[i]))
        
        # Basin interaction with varying curvature and coupling strength
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 2.0:
                basin_term += 0.2 * x[i]**4 + 0.1 * np.sin(5 * x[i])
            else:
                basin_term += 0.3 * np.abs(x[i])**3 + 0.05 * np.cos(3 * x[i])
        
        # Adaptive ridge structure with multiple overlapping peaks
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += 0.15 * (np.sin(2.0 * x[i]) + 0.5 * np.sin(4.0 * x[i]) + 0.3 * np.sin(6.0 * x[i]))
        
        return trig_term + elliptic_term + coupling_term + noise_term + harmonic_term + basin_term + ridge_term