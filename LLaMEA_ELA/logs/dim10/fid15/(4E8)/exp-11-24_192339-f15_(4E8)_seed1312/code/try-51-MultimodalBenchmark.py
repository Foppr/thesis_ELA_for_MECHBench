import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced polynomial base term with mixed degrees and adaptive coefficients
        poly_term = np.sum(0.8 * x_normalized**6 + 0.5 * x_normalized**5 + 0.3 * x_normalized**4 + 0.1 * x_normalized**3)
        
        # Complex trigonometric components with multiple frequencies and phase shifts
        trig_term1 = np.sum(np.sin(7 * np.pi * x_normalized) * np.cos(5 * np.pi * x_normalized) * np.sin(3 * np.pi * x_normalized))
        trig_term2 = np.sum(np.cos(4 * np.pi * x_normalized) * np.sin(6 * np.pi * x_normalized) * np.cos(2 * np.pi * x_normalized))
        
        # Enhanced radial basis function components with dynamic centers and variable widths
        centers = np.linspace(-0.8, 0.8, min(7, self.dim))
        rbfs = []
        for i in range(min(7, self.dim)):
            center = centers[i]
            width = 0.3 + 0.7 * (i / max(1, self.dim - 1))
            rbf = np.exp(-width * (x_normalized - center)**2) * (1 + 0.2 * np.sin(5 * np.pi * center))
            rbfs.append(rbf)
        rbf_term = np.sum(np.array(rbfs))
        
        # Advanced cross-terms creating complex interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(3 * np.pi * (x_normalized[i] + x_normalized[j])) * 
                              np.cos(4 * np.pi * (x_normalized[i] - x_normalized[j])) * 
                              np.exp(-0.5 * (x_normalized[i]**2 + x_normalized[j]**2)))
        
        # Exponential decay with dimension-dependent scaling and additional sinusoidal modulation
        exp_decay = np.sum(np.exp(-0.3 * x_normalized**2) * (1 + 0.15 * np.abs(x_normalized) + 0.05 * np.sin(8 * np.pi * x_normalized)))
        
        # Additional global structure term with multiple local minima
        global_term = 0.0
        for i in range(self.dim):
            global_term += (np.sin(2 * np.pi * x_normalized[i]) + 
                           0.5 * np.sin(4 * np.pi * x_normalized[i]) + 
                           0.3 * np.sin(6 * np.pi * x_normalized[i]))
        
        # Combine all terms with appropriate weights
        return (poly_term + 0.4 * trig_term1 + 0.3 * trig_term2 + 0.15 * rbf_term + 
                0.08 * cross_term + 0.12 * exp_decay + 0.05 * global_term)