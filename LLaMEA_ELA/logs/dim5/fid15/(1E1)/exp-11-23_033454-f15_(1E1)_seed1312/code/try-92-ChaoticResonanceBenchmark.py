import numpy as np

class ChaoticResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Precompute global minima positions for 2D case
        if dim == 2:
            # Create a grid of global minima with chaotic spacing
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
        
        # Quadratic basin term with dynamic conditioning
        basin_term = 0.1 * np.sum(x**2)
        
        # Multimodal term with chaotic harmonic resonance
        multimodal_term = 0.0
        
        if self.dim == 2:
            # For 2D, use a complex harmonic resonance pattern with chaotic modulation
            for i, min_pos in enumerate(self.global_minima):
                dist = np.sqrt((x[0] - min_pos[0])**2 + (x[1] - min_pos[1])**2)
                # Chaotic modulation via sine and cosine with dynamic frequency
                freq = 2.0 + 0.5 * np.sin(i * 0.5 + x[0] * 0.3)
                phase = 0.5 * np.cos(x[1] * 0.4 + i * 0.2)
                resonance = np.sin(freq * dist + phase) * np.exp(-dist**2 / 2.0)
                # Dynamic amplitude modulation
                amp_mod = 1.0 + 0.3 * np.sin(i * 0.7 + x[1] * 0.5)
                multimodal_term += amp_mod * resonance
        else:
            # For higher dimensions, use a chaotic harmonic network with adaptive coupling
            for i in range(0, self.dim, 2):
                if i + 1 < self.dim:
                    dist = np.sqrt((x[i] - 1.0)**2 + (x[i+1] - 1.0)**2)
                    # Chaotic modulation using dynamic sine frequency
                    freq = 1.5 + 0.4 * np.sin(i * 0.3 + x[i] * 0.2 + x[i+1] * 0.1)
                    phase = 0.3 * np.cos(x[i] * 0.5 + x[i+1] * 0.4)
                    resonance = np.sin(freq * dist + phase) * np.exp(-dist**2 / 1.5)
                    # Adaptive coupling strength
                    coupling_strength = 0.7 + 0.3 * np.cos(i * 0.2 + x[i] * 0.1)
                    multimodal_term += coupling_strength * resonance
                    
                    dist = np.sqrt((x[i] + 1.0)**2 + (x[i+1] + 1.0)**2)
                    resonance = np.sin(freq * dist + phase) * np.exp(-dist**2 / 1.5)
                    multimodal_term += coupling_strength * resonance
            
            # Add cross-dimensional harmonic interference
            for i in range(min(4, self.dim)):
                if i + 3 < self.dim:
                    dist = np.sqrt((x[i] - 0.5)**2 + (x[i+3] - 0.5)**2)
                    freq = 1.8 + 0.2 * np.sin(i * 0.4 + x[i+1] * 0.3)
                    phase = 0.4 * np.sin(x[i+2] * 0.6)
                    resonance = np.cos(freq * dist + phase) * np.exp(-dist**2 / 1.2)
                    multimodal_term += 0.5 * resonance
                    
                    dist = np.sqrt((x[i] + 0.5)**2 + (x[i+3] + 0.5)**2)
                    resonance = np.cos(freq * dist + phase) * np.exp(-dist**2 / 1.2)
                    multimodal_term += 0.5 * resonance
            
            # Add a dynamic harmonic term with time-varying frequency modulation
            for i in range(self.dim):
                # Dynamic frequency based on position and dimension index
                freq = 2.0 + 0.3 * np.sin(i * 0.5 + x[i] * 0.4)
                phase = 0.6 * np.cos(x[i] * 0.7 + i * 0.3)
                dist = np.abs(x[i] - 1.0)
                resonance = np.sin(freq * dist + phase) * np.exp(-dist**2 / 1.0)
                multimodal_term += 0.8 * resonance
        
        # Add dynamic conditioning with time-varying weights
        condition_term = 0.0
        for i in range(self.dim):
            # Dynamic weight based on dimension index and variable values
            weight = 1.0 + 0.4 * np.sin(i * 0.3 + x[i] * 0.2)
            condition_term += weight * (i + 1) * x[i]**4
        
        # Combine all terms with different weights
        return basin_term + condition_term - multimodal_term