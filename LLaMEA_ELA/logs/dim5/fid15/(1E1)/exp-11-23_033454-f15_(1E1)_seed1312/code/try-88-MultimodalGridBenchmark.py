import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Precompute global minima positions for 2D case
        if dim == 2:
            # Create grid of global minima with tighter spacing and varied heights
            grid_points = np.linspace(-4.5, 4.5, 9)
            for i in range(9):
                for j in range(9):
                    self.global_minima.append([grid_points[i], grid_points[j]])
        else:
            # For higher dimensions, create a more complex structure
            self.global_minima = [[0.0] * dim]
    
    def f(self, x):
        if len(x) != self.dim:
            # If dimension doesn't match, adjust x to fit
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with variable conditioning
        basin_term = 0.1 * np.sum(x**2)
        
        # Multimodal term with multiple global minima using chaotic logistic modulation
        multimodal_term = 0.0
        
        if self.dim == 2:
            # For 2D, use grid of global minima with varying decay rates and heights
            for i, min_pos in enumerate(self.global_minima):
                dist = np.sqrt((x[0] - min_pos[0])**2 + (x[1] - min_pos[1])**2)
                # Use chaotic modulation via logistic map for decay rate
                r = 3.95 + 0.05 * np.sin(i * 0.4 + x[0] * 0.1 + np.cos(x[1] * 0.2))
                logistic_mod = 1.0 / (1.0 + np.exp(-r * (dist - 2.0)))
                decay_rate = 0.15 + 0.35 * logistic_mod
                height = 0.6 + 0.4 * np.cos(i * 0.25 + x[1] * 0.1 + np.sin(x[0] * 0.3))
                multimodal_term += height * np.exp(-dist**2 / decay_rate)
        else:
            # For higher dimensions, use complex cross-dimensional interaction terms
            # Add interaction between pairs of dimensions with chaotic modulation
            for i in range(0, self.dim, 2):
                if i + 1 < self.dim:
                    dist = np.sqrt((x[i] - 2.0)**2 + (x[i+1] - 2.0)**2)
                    # Chaotic modulation using logistic map with time-varying parameters
                    r = 3.8 + 0.2 * np.sin(i * 0.3 + x[i] * 0.2 + np.cos(x[i+1] * 0.1))
                    logistic_mod = 1.0 / (1.0 + np.exp(-r * (dist - 1.5)))
                    strength = 0.6 + 0.4 * logistic_mod
                    phase = 0.5 * np.cos(x[i+1] * 0.3 + np.sin(x[i] * 0.2))
                    multimodal_term += strength * np.exp(-dist**2 / (0.4 + phase))
                    dist = np.sqrt((x[i] + 2.0)**2 + (x[i+1] + 2.0)**2)
                    multimodal_term += strength * np.exp(-dist**2 / (0.4 + phase))
            
            # Add additional interaction terms between non-adjacent dimensions with chaotic phases
            for i in range(min(3, self.dim)):
                if i + 2 < self.dim:
                    dist = np.sqrt((x[i] - 1.0)**2 + (x[i+2] - 1.0)**2)
                    # Chaotic modulation using logistic map with time-varying parameters
                    r = 3.7 + 0.3 * np.cos(i * 0.5 + x[i+1] * 0.2 + np.sin(x[i] * 0.1))
                    logistic_mod = 1.0 / (1.0 + np.exp(-r * (dist - 1.0)))
                    strength = 0.5 + 0.3 * logistic_mod
                    phase = 0.4 * np.sin(x[i] * 0.4 + np.cos(x[i+2] * 0.3))
                    multimodal_term += strength * np.exp(-dist**2 / (0.6 + phase))
                    dist = np.sqrt((x[i] + 1.0)**2 + (x[i+2] + 1.0)**2)
                    multimodal_term += strength * np.exp(-dist**2 / (0.6 + phase))
            
            # Add a complex interaction term with chaotic sinusoidal pattern and dynamic modulation
            for i in range(self.dim):
                if i + 1 < self.dim:
                    # Create a chaotic modulation to the interaction using logistic map with time-varying parameters
                    r = 3.9 + 0.1 * np.sin(x[i] * 0.6 + x[i+1] * 0.3 + np.cos(x[i] * 0.2))
                    logistic_mod = 1.0 / (1.0 + np.exp(-r * (np.abs(x[i]) - 1.0)))
                    modulation = 1.0 + 0.4 * logistic_mod
                    dist = np.sqrt((x[i] - 1.5)**2 + (x[i+1] - 1.5)**2)
                    multimodal_term += modulation * np.exp(-dist**2 / (0.5 + 0.2 * np.cos(x[i] * 0.4 + np.sin(x[i+1] * 0.3))))
        
        # Add a complex conditioning term that varies across dimensions with dynamic scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Dynamic scaling factor based on dimension index and variable values with chaotic modulation
            scale_factor = 1.0 + 0.5 * np.sin(i * 0.3 + x[i] * 0.2 + np.cos(x[i] * 0.1))
            condition_term += scale_factor * (i + 1) * x[i]**4
        
        # Add time-varying chaotic modulation to the entire function
        time_mod = 1.0 + 0.1 * np.sin(np.sum(x) * 0.5)
        
        # Combine all terms with different weights
        return basin_term * time_mod + condition_term - multimodal_term