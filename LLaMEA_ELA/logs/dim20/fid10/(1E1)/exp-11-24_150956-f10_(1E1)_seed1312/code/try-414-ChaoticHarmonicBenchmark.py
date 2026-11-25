import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map chaotic sequence for dimensionality
        self.logistic_seq = np.array([0.5])
        for i in range(dim + 100):
            next_val = 3.9 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[100:]
        
    def f(self, x):
        # Scale input to [-1, 1]
        x_scaled = x / 5.0
        
        # Chaotic component using logistic map
        chaotic = np.sum(self.logistic_seq[:self.dim] * np.sin(10.0 * x_scaled))
        
        # Spherical harmonics component
        spherical = np.sum((x_scaled**2 + 0.1) * np.cos(5.0 * np.arctan2(x_scaled[1], x_scaled[0]) + 
                                                       2.0 * np.log(np.sqrt(x_scaled[0]**2 + x_scaled[1]**2) + 1e-8)))
        
        # Radial basis function with varying widths and centers
        rbf = 0.0
        centers = np.linspace(-1, 1, 5)
        for i in range(5):
            for j in range(5):
                center = np.array([centers[i], centers[j]])
                width = 0.2 + 0.3 * np.sin(i + j)
                rbf += np.exp(-0.5 * np.sum(((x_scaled - center) / width)**2))
        
        # Multi-scale sinusoidal interference
        multiscale = np.sum(np.sin(20.0 * x_scaled) * np.cos(15.0 * x_scaled) + 
                           0.5 * np.sin(35.0 * x_scaled**2) * np.cos(25.0 * x_scaled**2) + 
                           0.3 * np.sin(50.0 * x_scaled**3) * np.cos(40.0 * x_scaled**3))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += np.exp(-2.0 * np.abs(x_scaled[i] - x_scaled[i+1])) * \
                             (x_scaled[i]**2 + x_scaled[i+1]**2)
        
        # Asymmetric potential with polynomial terms
        potential = np.sum(0.5 * x_scaled**4 + 0.3 * x_scaled**3 + 0.7 * x_scaled**2 + 
                          0.1 * x_scaled + 0.2 * np.sin(8.0 * x_scaled))
        
        return 0.25 * chaotic + 0.2 * spherical + 0.15 * rbf + 0.2 * multiscale + \
               0.1 * cross_coupling + 0.1 * potential + 2.1