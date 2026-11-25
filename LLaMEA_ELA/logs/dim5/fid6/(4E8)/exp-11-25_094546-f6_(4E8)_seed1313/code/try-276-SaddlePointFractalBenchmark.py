import numpy as np

class SaddlePointFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced fractal parameters with temporal dynamics
        self.fractal_exp = np.random.rand(dim) * 0.8 + 0.3
        self.saddle_params = np.random.rand(dim) * 3.0 + 1.5
        self.coupling_strength = np.random.rand(dim, dim) * 0.5 + 0.2
        # Temporal modulation parameters
        self.temporal_phase = np.random.rand(dim) * 2.0 * np.pi
        self.resonance_freq = np.random.rand(dim) * 0.5 + 0.1
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced fractal-like curvature with temporal modulation
            fractal_curvature = 0.0
            for j in range(min(20, self.dim)):
                phase = self.temporal_phase[i] + j * 0.1
                fractal_curvature += (np.abs(xi)**(1.0 + self.fractal_exp[i] * np.sin(phase))) * \
                                   np.cos(xi * (j + 1) * 2.0 + phase)
            
            # Enhanced saddle point dominance with chaotic interactions
            saddle_force = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic interaction term
                    chaotic_term = np.sin(xi * x_norm[j] * (i + j + 1)) * \
                                  np.exp(-0.5 * (xi - x_norm[j])**2)
                    saddle_force += self.saddle_params[j] * np.tanh(xi - x_norm[j]) * chaotic_term
            
            # Dynamic coupling with resonance effects
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Resonance modulation
                    resonance = np.sin(self.resonance_freq[i] * (xi + x_norm[j]))
                    coupling += self.coupling_strength[i, j] * \
                               np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j]) * resonance
            
            # Multi-scale oscillatory behavior with chaotic phase shifts
            oscillatory = 0.0
            for k in range(1, min(25, self.dim + 10)):
                # Chaotic phase modulation
                phase_mod = np.sin(k * self.temporal_phase[i] + k * 0.5)
                oscillatory += (1.0 / k**1.8) * np.sin(k * xi + k * np.cos(i * 0.7 + phase_mod))
            
            # Additional chaotic cross-dimensional terms
            cross_term = 0.0
            for j in range(self.dim):
                if i != j:
                    cross_term += np.sin(xi * x_norm[j] * (i + 1)) * \
                                np.cos(x_norm[j] * (i + j + 1))
            
            # Combine terms with adaptive weighting and chaotic scaling
            weight = 1.0 + 0.3 * np.sin(i * 0.9) * np.cos(self.dim * 0.4)
            chaos_factor = 1.0 + 0.2 * np.sin(np.sum(x_norm) * 0.5)
            
            # Enhanced saddle point dominance with fractal structure and chaos
            term = (weight * (fractal_curvature + saddle_force + coupling + oscillatory + cross_term)**2 + 
                   0.15 * np.abs(xi)**3.5 + 0.08 * xi**5 + 
                   0.05 * np.sin(xi * 10) * np.cos(xi * 7))
            
            result += term * chaos_factor
            
        # Global scaling with enhanced fractal dimension correction and temporal effects
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 4.0) + \
                      0.2 * np.cos(np.log(self.dim + 1) * 3.5) + \
                      0.1 * np.sin(np.sum(x_norm) * 0.3)
        
        return global_scale * result / self.dim