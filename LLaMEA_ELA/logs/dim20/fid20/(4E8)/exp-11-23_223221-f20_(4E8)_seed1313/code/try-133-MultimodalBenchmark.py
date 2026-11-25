import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function components with adaptive widths and centers
        rbf_term = 0.0
        num_centers = min(10, self.dim * 2)
        centers = np.random.uniform(-4.0, 4.0, (num_centers, self.dim))
        widths = np.random.uniform(0.5, 2.0, num_centers)
        
        for i in range(num_centers):
            dist = np.sum((x - centers[i])**2)
            rbf_term += widths[i] * np.exp(-dist / (2 * widths[i]**2))
        
        # Trigonometric periodic components with varying frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i)
            amp = 1.0 + 0.3 * np.cos(i)
            trig_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Cross-dimensional coupling with adaptive weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.sin(0.3 * (i + j))
                coupling_term += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Adaptive polynomial with mixed exponents and chaotic modulation
        poly_term = 0.0
        for i in range(self.dim):
            exp_factor = 1.5 + 0.8 * np.sin(0.7 * i)
            poly_term += (x[i]**exp_factor + 0.3 * x[i]**4 + 0.1 * x[i]**6) * np.cos(0.5 * x[i])
        
        # Fractal-like self-similar structure with multi-scale interactions
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 2.0 + np.sin(i)
            fractal_term += scale * np.sin(x[i] / (1.0 + np.abs(x[i]))) * np.cos(x[i] / (2.0 + x[i]**2))
        
        # Global conditioning term with exponential decay and harmonic mixing
        global_term = 0.0
        for i in range(self.dim):
            global_term += (0.8 * np.exp(-0.1 * x[i]**2) * np.sin(3.0 * x[i]) + 
                           0.2 * np.cos(2.0 * x[i]) * np.sin(x[i]) + 
                           0.1 * np.log(1.0 + x[i]**2))
        
        # Add noise component for increased landscape irregularity
        noise = 0.05 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x) + 0.3 * np.sin(5.0 * x))
        
        # Combine all terms with adaptive weighting
        return (0.6 * rbf_term + 0.4 * trig_term + 0.3 * coupling_term + 
                0.5 * poly_term + 0.2 * fractal_term + 0.4 * global_term + noise + 
                0.01 * np.sum(x**2))