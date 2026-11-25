import numpy as np

class ChaoticGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for dynamic behavior
        self.c1 = np.random.rand(dim) * 2 - 1
        self.c2 = np.random.rand(dim) * 3 + 1
        self.c3 = np.random.rand(dim) * 0.5 + 0.5
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with variable conditioning
        quad_term = 0.0
        for i in range(self.dim):
            quad_term += self.c1[i] * x[i]**2
            
        # Chaotic sine-wave modulation with dynamic frequency
        chaotic_mod = 0.0
        for i in range(self.dim):
            freq = 6.0 + 2.0 * np.sin(x[i] * 0.7)
            chaotic_mod += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Multi-scale harmonic interaction with adaptive amplitudes
        harmonic_interaction = 0.0
        for i in range(self.dim):
            amp = 1.5 + 2.0 * np.sin(i * 0.4)
            for j in range(i+1, self.dim):
                amp_ij = amp * (1.0 + 0.3 * np.cos(i * j * 0.3))
                harmonic_interaction += amp_ij * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Saddle-point potential with dimension-dependent control
        saddle_potential = 0.0
        for i in range(self.dim):
            saddle_potential += self.c2[i] * x[i]**3 + self.c3[i] * x[i]**5
            
        # Implicit constraint penalty (non-zero when outside [-5,5])
        penalty = 0.0
        for i in range(self.dim):
            if x[i] < -5 or x[i] > 5:
                penalty += 150 * (abs(x[i]) - 5)**2
                
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x[i] - x[j])
                cross_coupling += np.exp(-dist * 0.5) * np.sin(3 * (x[i] + x[j]))
                
        # Dynamic curvature modulation based on input values
        curvature_mod = 0.0
        for i in range(self.dim):
            curvature_mod += (1.0 + 0.5 * np.sin(x[i])) * x[i]**5
            
        # Final function value with weighted components
        return 0.6 * quad_term + 0.8 * chaotic_mod + 0.7 * harmonic_interaction + \
               0.5 * saddle_potential + 0.9 * penalty + 0.4 * cross_coupling + 1.0 * curvature_mod