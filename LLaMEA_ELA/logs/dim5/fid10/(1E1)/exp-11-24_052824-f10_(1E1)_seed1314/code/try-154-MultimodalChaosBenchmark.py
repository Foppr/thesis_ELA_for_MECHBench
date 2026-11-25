import numpy as np

class MultimodalChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and widths for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            rbf += np.exp(-self.widths[i] * np.sum(diff**2))
        
        # Trigonometric chaos component with dynamic frequencies
        trig_chaos = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(x[i])
            trig_chaos += np.sin(freq * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Adaptive conditioning based on dimensionality
        condition = 1.0
        if self.dim > 5:
            condition = 1.0 + 0.3 * np.sin(self.dim / 2.0)
            
        # Coupling terms with chaotic modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling += (x[i]**2 + x[j]**2) * np.sin(0.5 * x[i] * x[j]) * \
                           np.cos(0.3 * (x[i]**2 - x[j]**2)) * \
                           (1.0 + 0.2 * np.sin(x[i] + x[j]))
                
        # Multi-scale sinusoidal modulation with varying amplitudes
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += (np.sin(3.0 * x[i]) + 0.5 * np.sin(9.0 * x[i]) + 
                           0.2 * np.sin(27.0 * x[i])) * \
                          (1.0 + 0.3 * np.cos(x[i]))
        
        # Saddle-like structure with exponential scaling
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**4 - 6.0 * x[i]**2) * np.exp(-0.2 * x[i]**2)
            
        # Asymmetric component to break symmetry
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i]**3 + 0.5 * x[i]**2) * np.sin(1.5 * x[i])
        
        # Combine all components with dynamic weights based on dimensionality
        weight_rbf = 0.25 * condition
        weight_trig = 0.20 * (1.0 + 0.1 * np.cos(self.dim))
        weight_coupling = 0.15 * (1.0 + 0.05 * np.sin(self.dim))
        weight_multi = 0.20 * (1.0 + 0.2 * np.tanh(x[0] if self.dim > 0 else 0))
        weight_saddle = 0.10 * (1.0 + 0.15 * np.cos(self.dim / 3.0))
        weight_asymmetry = 0.10
        
        return (weight_rbf * rbf + 
                weight_trig * trig_chaos + 
                weight_coupling * coupling + 
                weight_multi * multi_scale + 
                weight_saddle * saddle + 
                weight_asymmetry * asymmetry)