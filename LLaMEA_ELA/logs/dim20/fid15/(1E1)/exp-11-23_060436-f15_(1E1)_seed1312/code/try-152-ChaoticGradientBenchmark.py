import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component with enhanced conditioning
        quadratic = np.sum(x**2) * 0.15
        
        # Enhanced chaotic gradient component with recursive fractal structure
        chaotic_grad = 0
        for i in range(self.dim):
            # Multi-scale chaotic mappings with recursive frequency modulation
            freq1 = 3.0 + 0.5 * np.sin(i * 0.8) * np.cos(0.3 * i)
            freq2 = 2.5 + 0.3 * np.cos(i * 1.1) * np.sin(0.4 * i)
            freq3 = 3.5 + 0.4 * np.sin(0.6 * i) * np.cos(0.2 * i)
            
            # Fractal-like chaotic terms with self-similar patterns
            term1 = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.5 * x[i]**2)
            term2 = np.cos(freq3 * x[i]) * np.sin(freq1 * x[i]) * np.exp(-0.3 * (x[i] - 2.0)**2)
            term3 = np.sin(freq2 * x[i]) * np.cos(freq3 * x[i]) * np.exp(-0.4 * (x[i] + 1.8)**2)
            
            # Recursive memory effect with chaotic coupling
            memory_factor = 0.15 * np.sin(0.25 * i) * np.cos(0.1 * i) if i > 0 else 0
            chaotic_grad += (term1 + term2 + term3) * (1.0 + 0.3 * np.sin(0.35 * i) + memory_factor)
        
        # Saddle point component with fractal scaling and dynamic locations
        saddle = 0
        for i in range(self.dim):
            # Fractal-based saddle point locations with recursive scaling
            saddle_loc = 2.5 * np.sin(i * 0.6) * (1.0 + 0.15 * np.cos(i * 0.4)) * np.exp(-0.1 * i)
            condition_factor = 1.0 + 0.5 * np.cos(i * 0.4) * np.sin(0.25 * i)
            
            # Fractal saddle point function with recursive curvature
            saddle_term = (x[i] - saddle_loc)**2 * (x[i] - saddle_loc)**4 * condition_factor
            saddle += saddle_term
        
        # Multi-scale oscillatory component with fractal modulation and chaotic interference
        oscillatory = 0
        scales = [0.5, 1.0, 1.8, 2.7, 3.5, 4.2, 5.0]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            
            # Multi-frequency oscillation with fractal amplitude modulation
            osc_term = np.sin(scale * x[i]) * np.cos(1.5 * scale * x[i]) * np.exp(-0.1 * (x[i] - 2.0)**2)
            osc_term += np.cos(scale * x[i]) * np.sin(2.0 * scale * x[i]) * np.exp(-0.15 * (x[i] + 2.0)**2)
            
            # Fractal chaos modulation with recursive scaling
            chaos_mod = 0.15 * np.sin(0.5 * scale * x[i]) * np.cos(0.2 * scale * x[i])
            osc_term += chaos_mod
            
            oscillatory += osc_term * (1.0 + 0.15 * np.sin(i * 0.45) * np.cos(0.3 * i))
        
        # Cross-dimensional interaction with fractal coupling weights
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended interaction range
                # Fractal-based dynamic weights with recursive scaling
                weight = 0.8 + 0.2 * np.sin(0.2 * (i + j)) * np.cos(0.15 * i) * np.exp(-0.05 * (i + j))
                interaction += weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Variable dimension coupling with fractal scaling and chaotic modulation
        coupling = 0
        for i in range(self.dim):
            # Fractal coupling factor with recursive self-similarity
            coupling_factor = 1.0 + 0.4 * np.sin(0.4 * i) * np.cos(0.3 * i) * np.exp(-0.02 * i)
            coupling += (np.sin(x[i] * coupling_factor) * np.cos(x[i] * coupling_factor) * 
                        np.exp(-0.2 * x[i]**2) * coupling_factor)
        
        # Asymmetric chaotic modulation with fractal complexity
        asymmetric = 0
        for i in range(self.dim):
            # Fractal-based asymmetry factor with recursive scaling
            asym_factor = 1.0 + 0.4 * np.sin(0.3 * i) * np.cos(0.2 * i) * np.exp(-0.03 * i)
            asym_term = (np.sin(x[i] * asym_factor) * np.exp(-0.1 * x[i]**2) + 
                        np.cos(x[i] * asym_factor) * np.exp(-0.15 * x[i]**2))
            asymmetric += asym_term
        
        # Hybrid polynomial-chaotic with fractal memory and enhanced multimodal structure
        memory = 0
        for i in range(self.dim):
            # Fractal memory effect with recursive coupling
            mem_factor = 0.25 * np.sin(0.1 * i) * np.cos(0.05 * i)
            memory += (np.sin(x[i]**3) * np.cos(x[i]) * np.exp(-0.1 * (x[i] - 1.5)**2) + 
                      np.cos(x[i]**2) * np.sin(x[i]) * np.exp(-0.15 * (x[i] + 1.5)**2) + mem_factor)
        
        # Enhanced multimodal structure with fractal peak clustering
        multimodal = 0
        for i in range(self.dim):
            # Fractal peak locations and heights with recursive scaling
            peak_loc = 2.0 * np.sin(0.3 * i) * (1.0 + 0.15 * np.cos(i * 0.25)) * np.exp(-0.01 * i)
            peak_height = 1.2 + 0.4 * np.cos(0.2 * i) * np.sin(0.1 * i) * np.exp(-0.02 * i)
            
            # Multi-peak fractal function with recursive distances
            multimodal += peak_height * (np.sin(x[i] - peak_loc) * np.exp(-0.2 * (x[i] - peak_loc)**2) +
                                       np.cos(x[i] + peak_loc) * np.exp(-0.15 * (x[i] + peak_loc)**2))
        
        # Fractal-like chaotic structure with recursive self-similarity
        fractal = 0
        for i in range(self.dim):
            # Recursive fractal modulation using self-similar patterns
            fractal_term = np.sin(x[i]**2) * np.cos(x[i]) * np.exp(-0.1 * x[i]**2)
            fractal_term += np.cos(x[i]**3) * np.sin(x[i]) * np.exp(-0.05 * (x[i] - 1.5)**2)
            fractal += fractal_term * (1.0 + 0.25 * np.sin(0.4 * i) * np.cos(0.1 * i))
        
        # Multi-scale chaotic interference patterns with recursive scaling
        interference = 0
        for i in range(self.dim):
            # Recursive interference between multiple chaotic frequencies
            freq_a = 1.5 + 0.5 * np.sin(i * 0.35) * np.cos(0.2 * i)
            freq_b = 2.5 + 0.3 * np.cos(i * 0.45) * np.sin(0.15 * i)
            interference += (np.sin(freq_a * x[i]) * np.cos(freq_b * x[i]) * 
                           np.exp(-0.1 * (x[i] - 0.8)**2) +
                           np.cos(freq_a * x[i]) * np.sin(freq_b * x[i]) * 
                           np.exp(-0.15 * (x[i] + 0.8)**2))
        
        # Enhanced gradient coupling with fractal scaling
        gradient_coupling = 0
        for i in range(self.dim):
            # Fractal-based coupling based on neighbor dimensions
            if i > 0:
                grad_coupling = np.sin(x[i-1] * x[i]) * np.cos(x[i-1] + x[i]) * np.exp(-0.1 * (x[i-1]**2 + x[i]**2))
                gradient_coupling += grad_coupling * (1.0 + 0.2 * np.sin(0.35 * i) * np.cos(0.1 * i))
        
        # Enhanced local minima clustering with fractal structure
        local_minima = 0
        for i in range(self.dim):
            # Fractal clustered local minima locations
            cluster_loc = 3.0 * np.sin(0.45 * i) * (1.0 + 0.15 * np.cos(i * 0.25)) * np.exp(-0.01 * i)
            cluster_height = 1.0 + 0.3 * np.cos(0.35 * i) * np.sin(0.2 * i) * np.exp(-0.02 * i)
            local_minima += cluster_height * (np.exp(-0.5 * (x[i] - cluster_loc)**2) + 
                                             np.exp(-0.3 * (x[i] + cluster_loc)**2))
        
        # Enhanced basin structure with fractal boundaries
        basins = 0
        for i in range(self.dim):
            # Fractal basin boundaries with varying depths and locations
            basin_loc = 1.8 * np.sin(0.35 * i) * (1.0 + 0.15 * np.cos(i * 0.25)) * np.exp(-0.01 * i)
            basin_depth = 0.9 + 0.25 * np.sin(0.45 * i) * np.cos(0.2 * i) * np.exp(-0.03 * i)
            basins += basin_depth * (np.exp(-0.3 * (x[i] - basin_loc)**2) + 
                                   np.exp(-0.2 * (x[i] + basin_loc)**2))
        
        # Multi-modal chaotic peak clustering with recursive scaling
        peak_clusters = 0
        for i in range(self.dim):
            # Fractal clustered peaks with recursive locations and heights
            cluster_center = 2.5 * np.sin(0.55 * i) * (1.0 + 0.15 * np.cos(i * 0.35)) * np.exp(-0.02 * i)
            cluster_height = 1.3 + 0.3 * np.sin(0.25 * i) * np.cos(0.15 * i) * np.exp(-0.02 * i)
            peak_clusters += cluster_height * (np.exp(-0.4 * (x[i] - cluster_center)**2) + 
                                              np.exp(-0.3 * (x[i] + cluster_center)**2))
        
        # Combine all components with optimized fractal weights
        return (quadratic * 0.8 +
                chaotic_grad * 0.6 +
                saddle * 0.4 +
                oscillatory * 0.7 +
                interaction * 0.35 +
                coupling * 0.2 +
                asymmetric * 0.3 +
                memory * 0.2 +
                multimodal * 0.35 +
                fractal * 0.2 +
                interference * 0.25 +
                gradient_coupling * 0.15 +
                local_minima * 0.2 +
                basins * 0.25 +
                peak_clusters * 0.2)