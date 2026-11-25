import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial chaos with exponential decay correlations
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Exponentially decaying harmonic terms
            exp_decay = np.exp(-0.1 * (i + 1))
            poly_term = xi**4 + 0.5 * xi**3 + 0.2 * xi**2 + 0.1 * xi
            harm_freq = 2.0 + 1.5 * np.sin(0.5 * self.t + i * 0.3)
            result += exp_decay * (poly_term + np.sin(harm_freq * xi))
            
        # Saddle-point clustering with time-varying potential wells
        cluster_strength = 1.5 + 0.8 * np.cos(0.7 * self.t)
        for i in range(self.dim):
            xi = x[i]
            # Clustered saddle points with varying depths
            depth = 2.0 + 1.0 * np.sin(0.4 * self.t + i * 0.5)
            width = 0.5 + 0.3 * np.cos(0.6 * self.t + i * 0.4)
            saddle = depth * (xi**2 - width)**2
            result += cluster_strength * saddle
            
        # Time-varying gradient coupling with chaotic modulation
        grad_coupling = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(max(0, i-1), min(i+1, self.dim)):
                if i != j:
                    coupling_strength = 0.3 + 0.2 * np.sin(0.8 * self.t + (i+j) * 0.2)
                    dist = abs(xi - x[j])
                    # Chaotic gradient interaction
                    grad_coupling += coupling_strength * np.exp(-dist**2) * \
                                   (xi**2 + x[j]**2) * np.sin(3.0 * (xi + x[j]) + 0.5 * self.t)
                    
        result += grad_coupling
        
        # Multi-scale chaotic oscillation with polynomial interactions
        chaos_amp = 1.0 + 0.5 * np.cos(0.9 * self.t)
        chaos_freq = 3.0 + 2.0 * np.sin(0.6 * self.t)
        chaos_term = 0.0
        for i in range(self.dim):
            phase_shift = 0.4 * np.sin(1.2 * self.t + i * 0.6) + \
                         0.3 * np.cos(0.8 * self.t + i * 0.5)
            chaos_term += chaos_amp * np.sin(chaos_freq * x[i] + phase_shift) * \
                         (x[i]**5 + 0.3 * x[i]**3 + 0.1 * x[i])
            
        # Adaptive weighting with chaotic coefficients
        w1 = 0.7 + 0.1 * np.sin(0.5 * self.t)
        w2 = 0.2 + 0.05 * np.cos(0.6 * self.t)
        
        result = w1 * result + w2 * chaos_term
        
        # Mutation: Added polynomial chaos interactions with exponential decay and enhanced clustering
        # Additional chaotic correlation term
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially correlated chaotic interaction
                corr_decay = np.exp(-0.2 * abs(i - j))
                phase_coupling = np.sin(2.5 * (x[i] + x[j]) + 0.6 * self.t) + \
                               0.4 * np.cos(1.8 * (x[i] - x[j]) + 0.7 * self.t)
                corr_term += corr_decay * phase_coupling * (x[i]**3 + x[j]**2)
                
        result += 0.5 * corr_term
        
        return result