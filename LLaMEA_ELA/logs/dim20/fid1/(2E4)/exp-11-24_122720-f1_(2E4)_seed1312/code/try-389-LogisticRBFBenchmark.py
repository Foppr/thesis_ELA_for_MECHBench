import numpy as np

class LogisticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logistic map parameters
        self.logistic_rates = np.random.uniform(3.5, 4.0, dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 5))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (dim, 5))
        # Asymmetric trigonometric coupling terms
        self.trig_amplitudes = np.random.uniform(0.5, 2.0, (dim, 3))
        self.trig_frequencies = np.random.uniform(1.0, 3.0, (dim, 3))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map component
        logistic_sum = 0
        for i in range(self.dim):
            # Apply logistic map iteration
            xi = x[i]
            for _ in range(10):  # Multiple iterations for chaos
                xi = self.logistic_rates[i] * xi * (1 - xi)
            logistic_sum += xi**2
        
        # Radial basis function component
        rbf_sum = 0
        for i in range(self.dim):
            rbf_term = 0
            for j in range(5):  # 5 RBFs per dimension
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                rbf_term += np.exp(-0.5 * ((x[i] - center) / width)**2)
            rbf_sum += rbf_term
        
        # Asymmetric trigonometric coupling
        trig_coupling_sum = 0
        for i in range(self.dim):
            x_i = x[i]
            trig_term = (self.trig_amplitudes[i, 0] * np.sin(self.trig_frequencies[i, 0] * x_i) +
                        self.trig_amplitudes[i, 1] * np.cos(self.trig_frequencies[i, 1] * x_i) +
                        self.trig_amplitudes[i, 2] * np.tan(self.trig_frequencies[i, 2] * x_i))
            trig_coupling_sum += np.abs(trig_term) * np.sign(x_i)
        
        # Combine all components
        result = (0.6 * logistic_sum + 
                 1.0 * rbf_sum + 
                 0.8 * trig_coupling_sum)
        
        return result