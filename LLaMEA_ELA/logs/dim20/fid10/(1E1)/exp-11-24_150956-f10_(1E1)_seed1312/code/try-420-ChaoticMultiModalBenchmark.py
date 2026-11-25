import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logistic map chaotic component
        chaotic = np.zeros_like(x_scaled)
        r = 3.95
        for i in range(100):  # Discard first 100 iterations
            chaotic = r * chaotic * (1 - chaotic)
        chaotic = r * chaotic * (1 - chaotic)  # Final iteration
        
        # Spherical harmonics component
        spherical = np.sum(np.sin(3.0 * x_scaled) * np.cos(2.0 * x_scaled) + 
                          np.cos(4.0 * x_scaled) * np.sin(5.0 * x_scaled))
        
        # Asymmetric bell peaks with varying widths and heights
        peaks = np.sum(0.8 * np.exp(-10.0 * (x_scaled - 0.2)**2) * 
                      (1 + 0.3 * np.sin(15.0 * x_scaled)) +
                      0.4 * np.exp(-5.0 * (x_scaled + 0.5)**2) * 
                      (1 + 0.5 * np.cos(12.0 * x_scaled)) +
                      0.6 * np.exp(-8.0 * (x_scaled - 0.8)**2) * 
                      (1 + 0.4 * np.sin(18.0 * x_scaled)))
        
        # Cross-dimensional coupling with chaotic modulation
        cross_coupling = np.sum(np.sin(x_scaled[:-1] * x_scaled[1:]) * 
                              (1 + 0.3 * chaotic[:-1] * chaotic[1:]))
        
        # Fractional polynomial interactions
        fractional = np.sum((x_scaled**1.5 + x_scaled**2.5) * 
                          np.sin(3.0 * x_scaled) + 
                          (x_scaled**0.7 + x_scaled**1.3) * 
                          np.cos(4.0 * x_scaled))
        
        # Combined landscape with chaotic weighting
        return 0.4 * peaks + 0.25 * spherical + 0.2 * cross_coupling + 0.1 * fractional + 0.05 * chaotic + 2.1