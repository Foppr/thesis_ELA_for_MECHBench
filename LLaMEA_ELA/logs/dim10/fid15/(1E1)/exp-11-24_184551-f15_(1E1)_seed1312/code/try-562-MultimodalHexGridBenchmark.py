import numpy as np

class MultimodalHexGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate hexagonal grid of global minima
        num_layers = 3
        radius = 3.0
        for layer in range(1, num_layers + 1):
            for i in range(layer):
                angle = 2 * np.pi * i / layer
                x = radius * layer * np.cos(angle)
                y = radius * layer * np.sin(angle)
                if x != 0 or y != 0:  # Skip center point
                    self.global_minima.append([x, y])
        
        # Add center minimum
        self.global_minima.append([0.0, 0.0])
        
        # Pad minima to match dimensions
        for i in range(len(self.global_minima)):
            while len(self.global_minima[i]) < self.dim:
                self.global_minima[i].append(0.0)
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = np.sum(x**2) * 0.05
        
        # Multimodal terms - multiple global minima in hexagonal grid
        multimodal_term = 0.0
        for i in range(len(self.global_minima)):
            min_point = self.global_minima[i]
            if len(min_point) != self.dim:
                continue
                
            # Use first two dimensions for the hex grid pattern, rest are zero
            distance = 0.0
            for j in range(min(2, self.dim)):
                distance += (x[j] - min_point[j])**2
            
            # Add contribution from this minimum
            multimodal_term += 1.0 / (1.0 + distance)
        
        # Add sinusoidal perturbations to make it non-trivial
        perturbation = np.sum(np.sin(x * 0.5) * 0.1)
        
        return basin_term - multimodal_term + perturbation