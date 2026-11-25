import numpy as np

class MultimodalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Enhanced trigonometric component with frequency modulation
        trig_term = 0
        for i in range(self.dim):
            freq1 = 8 + 0.5 * np.sin(2 * i)
            freq2 = 12 + 0.3 * np.cos(3 * i)
            trig_term += (np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[i]) + 
                         0.7 * np.sin(freq2 * x_norm[i]**2) * np.cos(freq1 * x_norm[i]**2))
        
        # Modified radial basis function with adaptive centers
        rbf_term = 0
        centers = [
            np.array([0.5, -0.3, 0.8]),
            np.array([-0.7, 0.6, -0.5]),
            np.array([0.4, 0.9, -0.7])
        ]
        
        for i in range(min(3, self.dim)):
            center = centers[i % len(centers)]
            if i < len(center):
                diff = x_norm[i] - center[i]
                rbf_term += (np.exp(-5 * diff**2) + 0.5 * np.exp(-3 * (diff - 0.5)**2) + 
                            0.3 * np.exp(-7 * (diff + 0.4)**2))
        
        # Enhanced saddle point component with nonlinear transformation
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += (x_norm[i]**4 - 2 * x_norm[i]**2) * (1 + 0.3 * np.sin(5 * x_norm[i]) + 
                                                               0.2 * np.cos(8 * x_norm[i]))
        
        # Coupling terms with varying interaction strengths
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                strength = 0.5 + 0.5 * np.sin(0.5 * (i + j))
                cross_term += strength * np.sin(3 * (x_norm[i] + x_norm[j])) * \
                             np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
        
        # Combined function with refined scaling
        result = 2.0 * trig_term + 1.0 * rbf_term + 1.6 * saddle_term + 0.8 * cross_term
        
        # Add small controlled noise
        noise = np.random.normal(0, 0.0005)
        
        return result + noise