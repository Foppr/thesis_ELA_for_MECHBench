import numpy as np

class ChaoticGaussianSpiralBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Logarithmic spiral Gaussian peaks with chaotic phase modulation
        peaks = []
        for i in range(self.dim):
            angle = np.pi * (i + 1) * np.exp(0.5 * x_norm[i])
            radius = 2.0 * np.exp(-0.3 * (x_norm[i]**2))
            peak_val = np.exp(-0.5 * ((x_norm[i] - radius * np.cos(angle))**2 + (x_norm[(i+1)%self.dim] - radius * np.sin(angle))**2) / 0.1)
            peaks.append(peak_val)
        
        f2 = np.sum(peaks)
        
        # Adaptive Gaussian terms with dimension-dependent variance
        variances = 0.5 + 0.3 * np.sin(np.pi * x_norm * self.dim)
        f3 = np.sum(np.exp(-0.5 * (x_norm**2) / variances))
        
        # Saddle-point structure with dynamic scaling
        saddle_terms = []
        for i in range(self.dim):
            j = (i + 1) % self.dim
            saddle_terms.append((x_norm[i]**2 - x_norm[j]**2) * np.cos(0.7 * np.pi * x_norm[i]))
        f4 = np.sum(saddle_terms)
        
        # Chaotic sine-cosine interaction with dynamic frequency modulation
        freq_mod = 1 + 0.5 * np.sin(0.3 * self.dim * x_norm)
        f5 = np.sum(np.sin(freq_mod * x_norm) * np.cos(freq_mod * x_norm**2))
        
        # Dynamic phase-shifted cosine terms with exponential decay
        phase_shifts = np.exp(-0.1 * np.abs(x_norm)) * np.sin(0.8 * np.pi * x_norm)
        f6 = np.sum(np.cos(x_norm + phase_shifts)**3)
        
        # Combine all components with dynamic weighting
        weights = [0.4, 0.25, 0.15, 0.1, 0.08, 0.02]
        total = weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5 + weights[5] * f6
        
        # Add a small fifth-order polynomial for fine-tuning
        f7 = np.sum(x_norm**5)
        
        return total - 0.01 * f7