import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial chaos with enhanced exponential decay correlations
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced exponentially decaying harmonic terms
            exp_decay = np.exp(-0.15 * (i + 1))
            poly_term = xi**4 + 0.6 * xi**3 + 0.3 * xi**2 + 0.15 * xi
            harm_freq = 2.5 + 2.0 * np.sin(0.6 * self.t + i * 0.35)
            result += exp_decay * (poly_term + np.sin(harm_freq * xi))
            
        # Enhanced saddle-point clustering with stronger time-varying potential wells
        cluster_strength = 2.0 + 1.2 * np.cos(0.8 * self.t)
        for i in range(self.dim):
            xi = x[i]
            # Enhanced clustered saddle points with varying depths and widths
            depth = 2.5 + 1.5 * np.sin(0.5 * self.t + i * 0.6)
            width = 0.6 + 0.4 * np.cos(0.7 * self.t + i * 0.5)
            saddle = depth * (xi**2 - width)**2
            result += cluster_strength * saddle
            
        # Enhanced time-varying gradient coupling with chaotic modulation
        grad_coupling = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(max(0, i-1), min(i+1, self.dim)):
                if i != j:
                    coupling_strength = 0.4 + 0.25 * np.sin(0.9 * self.t + (i+j) * 0.25)
                    dist = abs(xi - x[j])
                    # Enhanced chaotic gradient interaction
                    grad_coupling += coupling_strength * np.exp(-dist**2) * \
                                   (xi**2 + x[j]**2) * np.sin(3.5 * (xi + x[j]) + 0.6 * self.t)
                    
        result += grad_coupling
        
        # Enhanced multi-scale chaotic oscillation with polynomial interactions
        chaos_amp = 1.2 + 0.6 * np.cos(1.0 * self.t)
        chaos_freq = 3.5 + 2.5 * np.sin(0.7 * self.t)
        chaos_term = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(1.3 * self.t + i * 0.65) + \
                         0.4 * np.cos(0.9 * self.t + i * 0.55)
            chaos_term += chaos_amp * np.sin(chaos_freq * x[i] + phase_shift) * \
                         (x[i]**5 + 0.4 * x[i]**3 + 0.15 * x[i])
            
        # Enhanced adaptive weighting with chaotic coefficients
        w1 = 0.75 + 0.12 * np.sin(0.55 * self.t)
        w2 = 0.25 + 0.06 * np.cos(0.65 * self.t)
        
        result = w1 * result + w2 * chaos_term
        
        # Enhanced chaotic correlation term with modified interaction
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced exponentially correlated chaotic interaction
                corr_decay = np.exp(-0.25 * abs(i - j))
                phase_coupling = np.sin(2.8 * (x[i] + x[j]) + 0.7 * self.t) + \
                               0.5 * np.cos(2.0 * (x[i] - x[j]) + 0.8 * self.t)
                corr_term += corr_decay * phase_coupling * (x[i]**3 + x[j]**2)
                
        result += 0.6 * corr_term
        
        return result