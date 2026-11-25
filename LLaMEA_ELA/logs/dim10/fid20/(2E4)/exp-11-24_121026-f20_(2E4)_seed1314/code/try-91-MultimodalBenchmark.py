import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.c1 = 3.8
        self.c2 = 0.5
        self.c3 = 2.0
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine component with adaptive frequency
        chaotic_freq = 10 + 5 * np.sin(x_norm)
        f2 = np.sum(np.sin(chaotic_freq * x_norm)**4)
        
        # Multi-scale Gaussian peaks with varying heights
        peaks = []
        for i in range(1, 6):
            scale = i * 0.5
            peak_height = 1.0 / (i * 0.5)
            peaks.append(peak_height * np.exp(-scale * (x_norm - 0.2*i)**2))
        f3 = np.sum(np.array(peaks).sum(axis=0))
        
        # Hybrid polynomial-trigonometric term
        f4 = np.sum((x_norm**3 + 0.5 * np.sin(15 * x_norm))**2)
        
        # Cross-dimensional interaction with varying coupling strengths
        coupling = np.array([i * 0.1 for i in range(self.dim-1)])
        interaction = np.sum(coupling * (x_norm[:-1]**2 + x_norm[1:]**2))
        f5 = interaction
        
        # Fractional power chaotic modulation
        f6 = np.sum(np.abs(x_norm)**(1.7 + 0.3 * np.sin(20 * x_norm)))
        
        # Adaptive logistic map component
        logistic_map = []
        for i in range(self.dim):
            if i == 0:
                prev_val = x_norm[-1]
            else:
                prev_val = x_norm[i-1]
            log_val = self.c1 * prev_val * (1 - prev_val)
            logistic_map.append(log_val)
        f7 = np.sum(np.array(logistic_map)**2)
        
        # Multi-modal cosine component with varying amplitudes
        f8 = np.sum(0.5 * np.cos(20 * x_norm) + 0.3 * np.cos(40 * x_norm) + 0.2 * np.cos(60 * x_norm))
        
        # Combined nonlinear interaction terms
        f9 = np.sum(np.sin(x_norm) * np.cos(2 * x_norm) * np.tanh(x_norm))
        
        # Boundary repulsion with logarithmic scaling
        boundary_repulsion = np.sum(np.log(1 + 0.5 * x_norm**2))
        f10 = 0.3 * boundary_repulsion
        
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5 + 0.1 * f6 + 0.15 * f7 + 0.1 * f8 + 0.1 * f9 + 0.1 * f10