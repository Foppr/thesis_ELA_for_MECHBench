import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with dynamic frequency modulation
        chaotic_sine = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[i])
            chaotic_sine += np.sin(freq * x[i] + np.sin(x[i]**2)) * np.tanh(x[i])
        
        # Radial basis function with asymmetric Gaussian kernels
        rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                width = 1.0 + 0.3 * np.sin(0.5 * (x[i] + x[j]))
                asymmetry = 1.0 + 0.2 * np.sin(x[i] * x[j])
                rbf += asymmetry * np.exp(-0.5 * (dist / width)**2) * np.cos(dist)
        
        # Polynomial coupling with skewness and exponential scaling
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                skew = 1.0 + 0.5 * np.tanh(x[i] - x[j])
                term = (x[i]**2 + x[j]**2) * skew * np.exp(-0.1 * (x[i] - x[j])**2)
                poly_coupling += term
        
        # Asymmetric skewing mechanism with dynamic conditioning
        skew_term = 0
        for i in range(self.dim):
            skew_term += np.tanh(x[i]) * (1.0 + 0.3 * np.sin(0.5 * x[i])) * np.exp(-0.05 * x[i]**2)
        
        # Dynamic conditioning with polynomial scaling
        cond = 0
        for i in range(self.dim):
            cond += (x[i]**4 + 0.5 * x[i]**3) * np.tanh(x[i]) * (1.0 + 0.2 * np.cos(0.3 * x[i]))
        
        # Fractal-like noise component with multiple frequency bands
        noise = 0
        for i in range(self.dim):
            noise += 0.1 * np.sin(5 * x[i]) * np.cos(7 * x[i]) * np.tanh(2 * x[i])
        
        # Global scaling and skewing factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.1) + 0.2 * np.cos(self.dim * 0.05)
        
        # Combine all components with optimized weights
        return scale_factor * (0.4 * chaotic_sine + 0.3 * rbf + 0.2 * poly_coupling + 
                              0.1 * skew_term + 0.05 * cond) + noise